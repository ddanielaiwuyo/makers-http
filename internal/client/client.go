package main

import (
	"encoding/binary"
	"errors"
	"fmt"
	"io"
	"log"
	"net"
	pb "pac/protos/compiled"

	"github.com/google/uuid"
	"google.golang.org/protobuf/proto"
)

const headerLength = 4

func connect() {
	conn, err := net.Dial("tcp", "localhost:9223")
	if err != nil {
		log.Fatal("could not connect with server", err)
	}

	log.Println("you've touched the server")

	defer conn.Close()

	header := make([]byte, headerLength)
	for {
		n, err := conn.Read(header)
		if err != nil && errors.Is(err, io.EOF) {
			log.Println("server closed pipe", err)
			return
		} else if err != nil {
			log.Println("unexpected read error", err)
			return
		}
		log.Println("header read from server:", n)

		packetLength := binary.BigEndian.Uint32(header)
		log.Println("total-packet length:", packetLength)

		packet := make([]byte, packetLength)
		out, err := conn.Read(packet)
		if err != nil && errors.Is(err, io.EOF) {
			log.Println("server closed pipe", err)
			return
		} else if err != nil {
			log.Println("unexpected read error", err)
			return
		}

		log.Println("packet-length read from stream:", out)

		var response pb.Packet
		if err := proto.Unmarshal(packet, &response); err != nil {
			log.Println("could not marhsall server's response:", err)
			log.Printf("server's response:\n %s\n", packet)
			return
		}

		log.Printf("response:\n %+v\n", &response)

		log.Printf("from: %d\n dest: %d\n content:%s\n",
			response.From, response.Dest, response.Payload,
		)

		if err := writeToServer("", conn); err != nil {
			log.Println(err)
			return
		}

	}
}

func writeToServer(msg string, conn net.Conn) error {
	if len(msg) < 5 {
		msg = "Uhm, actually 🤓, it should contain sender id"
	}
	packet := pb.Packet{
		From: 1789,
		Dest: 0,
		Payload: &pb.Packet_Game{
			Game: &pb.GameMessage{
				Ssid: uuid.New().String(),
				Play: msg,
			},
		},
	}
	content, err := proto.Marshal(&packet)
	if err != nil {
		return fmt.Errorf("could not marhall msg pb %w", err)
	}

	// creating packet as 4bytes for header
	header := make([]byte, headerLength)
	binary.BigEndian.PutUint32(header, uint32(len(content)))

	wirePacket := append(header, content...)

	if _, err := conn.Write(wirePacket); err != nil {
		return fmt.Errorf("could not write to server %w", err)
	}

	return nil
}

func main() {
	connect()
}
