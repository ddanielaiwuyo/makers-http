package internal

import (
	"encoding/binary"
	"errors"
	"fmt"
	"io"
	"log"
	"net"
	pb "pac/protos/compiled"

	"google.golang.org/protobuf/proto"
)

type MessageType int32

const (
	PaintMessage MessageType = iota
	ChatMessage
	GameMessage
	NewGameMessage
)

const serverId = 9223

func NewMessage(msg string, msgType MessageType) ([]byte, error) {

	packet := pb.Packet{
		From: serverId,
		Dest: 1738,
		// Payload: &pb.ChatMessage{Content: msg},
		Payload: &pb.Packet_Chat{Chat: &pb.ChatMessage{Content: msg}},
	}

	out, err := proto.Marshal(&packet)
	if err != nil {
		return []byte{}, fmt.Errorf("could not marshall msg %w", err)
	}

	return out, nil
}

func createPacket(data []byte) []byte {
	// first 4 bytes should contain the len of the data to read
	packet := make([]byte, 4)
	binary.BigEndian.PutUint32(packet, uint32(len(data)))
	// 1 byte -> 8 bits -> 2^8 -> 128
	// 2bytes -> 16bits -> 2^16 (-1)
	packet = append(packet, data...)
	fmt.Println("created packet for data")
	return packet
}

const headerLength = 4

func StartServer() {
	ln, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", serverId))
	if err != nil {
		log.Fatal(err)
	}

	log.Println("server running on port", serverId)

	for {
		conn, err := ln.Accept()
		if err != nil {
			log.Println("error in accepting conn", err)
			continue
		}

		go func(conn net.Conn) {
			defer conn.Close()
			msg, err := NewMessage("hello dear socket\n", ChatMessage)
			if err != nil {
				log.Println(err)
				return
			}

			content := createPacket(msg)
			if _, err := conn.Write(content); err != nil {
				log.Println("error occured in writing to connection", err)
				return
			}
			header := make([]byte, headerLength)
			log.Println("reading...")
			for {
				n, err := conn.Read(header)
				if err != nil && errors.Is(err, io.EOF) {
					log.Println("while reading, client disconnected unannounced!", err)
					return
				} else if err != nil {
					log.Println("unexpected reading error", err)
					return
				}

				log.Println("header bytes read from client:", n)
				messageLength := binary.BigEndian.Uint32(header)

				response_packet := make([]byte, messageLength)
				var msg  = &pb.Packet{}
				out, err := conn.Read(response_packet)
				if err != nil {
					log.Println("error reading from client", err)
					return
				}

				log.Println("packet size read from client", out)

				// might not need to close the connection, simply warn them
				// although, in a game setting... but it might
				// be tedious to do so,
				// so we could assume that they tried something funny
				// and accliam the other person winner (too harsh)
				// but we might also want to check for max-payloads
				// do encyption and stuff LATER
				if err := proto.Unmarshal(response_packet, msg); err != nil {
					log.Println("error in unmarshalling packet from client", err)
					return
				}

				log.Println("msg from client:")
				log.Printf("\n %+v\n", msg)
				log.Println("closing connection")
				return

			}
		}(conn)
	}
}
