package main

import (
	"pac/internal"
	// "google.golang.org/protobuf/proto"
	// "google.golang.org/grpc/profiling/proto"
	// "google.golang.org/protobuf/proto"
)

func main() {
	internal.StartServer()
	// person := pb.Person{
	// 	Name:  "Blanko Memphis",
	// 	Id:    1738,
	// 	Email: "cassablanka",
	// 	Numbers: []*pb.Person_PhoneNumber{
	// 		{Number: "000-000-999", Type: pb.Person_PHONE_TYPE_HOME},
	// 	},
	// }
	//
	// out, err := proto.Marshal(&person)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	//
	// fmt.Printf("%b, %s\n", out, out)
	//
	// p := &pb.Person{}
	//
	// if err := proto.Unmarshal(out, p); err != nil {
	// 	log.Fatal(err)
	// }
	//
	// fmt.Printf("unmarshalled proto-%+v\n", p)
	//
	//
}
