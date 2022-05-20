// proto 文件主要用来声明参数以及服务函数，并不用来保存变量值以及函数运算！！！！

// 版本信息

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.0
// 	protoc        v3.20.1
// source: mytest.proto

// 路径信息

package address

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Gender int32

const (
	Gender_SECRET Gender = 0
	Gender_man    Gender = 1
	Gender_male   Gender = 1
	Gender_woman  Gender = 2
	Gender_female Gender = 2
)

// Enum value maps for Gender.
var (
	Gender_name = map[int32]string{
		0: "SECRET",
		1: "man",
		// Duplicate value: 1: "male",
		2: "woman",
		// Duplicate value: 2: "female",
	}
	Gender_value = map[string]int32{
		"SECRET": 0,
		"man":    1,
		"male":   1,
		"woman":  2,
		"female": 2,
	}
)

func (x Gender) Enum() *Gender {
	p := new(Gender)
	*p = x
	return p
}

func (x Gender) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Gender) Descriptor() protoreflect.EnumDescriptor {
	return file_mytest_proto_enumTypes[0].Descriptor()
}

func (Gender) Type() protoreflect.EnumType {
	return &file_mytest_proto_enumTypes[0]
}

func (x Gender) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Gender.Descriptor instead.
func (Gender) EnumDescriptor() ([]byte, []int) {
	return file_mytest_proto_rawDescGZIP(), []int{0}
}

type StudentRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id     int32  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Age    int32  `protobuf:"varint,2,opt,name=age,proto3" json:"age,omitempty"`
	Name   string `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	Gender Gender `protobuf:"varint,4,opt,name=gender,proto3,enum=address.Gender" json:"gender,omitempty"` // 定义枚举类型的字段
}

func (x *StudentRequest) Reset() {
	*x = StudentRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_mytest_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StudentRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StudentRequest) ProtoMessage() {}

func (x *StudentRequest) ProtoReflect() protoreflect.Message {
	mi := &file_mytest_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StudentRequest.ProtoReflect.Descriptor instead.
func (*StudentRequest) Descriptor() ([]byte, []int) {
	return file_mytest_proto_rawDescGZIP(), []int{0}
}

func (x *StudentRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *StudentRequest) GetAge() int32 {
	if x != nil {
		return x.Age
	}
	return 0
}

func (x *StudentRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *StudentRequest) GetGender() Gender {
	if x != nil {
		return x.Gender
	}
	return Gender_SECRET
}

type StudentResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	StudentRequestFields []*StudentRequest `protobuf:"bytes,1,rep,name=StudentRequestFields,proto3" json:"StudentRequestFields,omitempty"`
	Year                 int32             `protobuf:"varint,2,opt,name=year,proto3" json:"year,omitempty"`
}

func (x *StudentResponse) Reset() {
	*x = StudentResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_mytest_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *StudentResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*StudentResponse) ProtoMessage() {}

func (x *StudentResponse) ProtoReflect() protoreflect.Message {
	mi := &file_mytest_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use StudentResponse.ProtoReflect.Descriptor instead.
func (*StudentResponse) Descriptor() ([]byte, []int) {
	return file_mytest_proto_rawDescGZIP(), []int{1}
}

func (x *StudentResponse) GetStudentRequestFields() []*StudentRequest {
	if x != nil {
		return x.StudentRequestFields
	}
	return nil
}

func (x *StudentResponse) GetYear() int32 {
	if x != nil {
		return x.Year
	}
	return 0
}

var File_mytest_proto protoreflect.FileDescriptor

var file_mytest_proto_rawDesc = []byte{
	0x0a, 0x0c, 0x6d, 0x79, 0x74, 0x65, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x07,
	0x61, 0x64, 0x64, 0x72, 0x65, 0x73, 0x73, 0x22, 0x6f, 0x0a, 0x0e, 0x53, 0x74, 0x75, 0x64, 0x65,
	0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x10, 0x0a, 0x03, 0x61, 0x67, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x03, 0x61, 0x67, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12,
	0x27, 0x0a, 0x06, 0x67, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x18, 0x04, 0x20, 0x01, 0x28, 0x0e, 0x32,
	0x0f, 0x2e, 0x61, 0x64, 0x64, 0x72, 0x65, 0x73, 0x73, 0x2e, 0x47, 0x65, 0x6e, 0x64, 0x65, 0x72,
	0x52, 0x06, 0x67, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x22, 0x72, 0x0a, 0x0f, 0x53, 0x74, 0x75, 0x64,
	0x65, 0x6e, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x4b, 0x0a, 0x14, 0x53,
	0x74, 0x75, 0x64, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x46, 0x69, 0x65,
	0x6c, 0x64, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x61, 0x64, 0x64, 0x72,
	0x65, 0x73, 0x73, 0x2e, 0x53, 0x74, 0x75, 0x64, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x52, 0x14, 0x53, 0x74, 0x75, 0x64, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x12, 0x12, 0x0a, 0x04, 0x79, 0x65, 0x61, 0x72,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x04, 0x79, 0x65, 0x61, 0x72, 0x2a, 0x42, 0x0a, 0x06,
	0x47, 0x65, 0x6e, 0x64, 0x65, 0x72, 0x12, 0x0a, 0x0a, 0x06, 0x53, 0x45, 0x43, 0x52, 0x45, 0x54,
	0x10, 0x00, 0x12, 0x07, 0x0a, 0x03, 0x6d, 0x61, 0x6e, 0x10, 0x01, 0x12, 0x08, 0x0a, 0x04, 0x6d,
	0x61, 0x6c, 0x65, 0x10, 0x01, 0x12, 0x09, 0x0a, 0x05, 0x77, 0x6f, 0x6d, 0x61, 0x6e, 0x10, 0x02,
	0x12, 0x0a, 0x0a, 0x06, 0x66, 0x65, 0x6d, 0x61, 0x6c, 0x65, 0x10, 0x02, 0x1a, 0x02, 0x10, 0x01,
	0x32, 0x52, 0x0a, 0x10, 0x42, 0x69, 0x72, 0x74, 0x68, 0x59, 0x65, 0x61, 0x72, 0x53, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x12, 0x3e, 0x0a, 0x09, 0x42, 0x69, 0x72, 0x74, 0x68, 0x59, 0x65, 0x61,
	0x72, 0x12, 0x17, 0x2e, 0x61, 0x64, 0x64, 0x72, 0x65, 0x73, 0x73, 0x2e, 0x53, 0x74, 0x75, 0x64,
	0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x18, 0x2e, 0x61, 0x64, 0x64,
	0x72, 0x65, 0x73, 0x73, 0x2e, 0x53, 0x74, 0x75, 0x64, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x32, 0x5e, 0x0a, 0x16, 0x54, 0x77, 0x6f, 0x41, 0x66, 0x74, 0x65, 0x72,
	0x59, 0x65, 0x61, 0x72, 0x41, 0x67, 0x65, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x44,
	0x0a, 0x0f, 0x54, 0x77, 0x6f, 0x41, 0x66, 0x74, 0x65, 0x72, 0x59, 0x65, 0x61, 0x72, 0x41, 0x67,
	0x65, 0x12, 0x17, 0x2e, 0x61, 0x64, 0x64, 0x72, 0x65, 0x73, 0x73, 0x2e, 0x53, 0x74, 0x75, 0x64,
	0x65, 0x6e, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x18, 0x2e, 0x61, 0x64, 0x64,
	0x72, 0x65, 0x73, 0x73, 0x2e, 0x53, 0x74, 0x75, 0x64, 0x65, 0x6e, 0x74, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x42, 0x0a, 0x5a, 0x08, 0x2e, 0x2f, 0x6d, 0x79, 0x74, 0x65, 0x73, 0x74,
	0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_mytest_proto_rawDescOnce sync.Once
	file_mytest_proto_rawDescData = file_mytest_proto_rawDesc
)

func file_mytest_proto_rawDescGZIP() []byte {
	file_mytest_proto_rawDescOnce.Do(func() {
		file_mytest_proto_rawDescData = protoimpl.X.CompressGZIP(file_mytest_proto_rawDescData)
	})
	return file_mytest_proto_rawDescData
}

var file_mytest_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_mytest_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_mytest_proto_goTypes = []interface{}{
	(Gender)(0),             // 0: address.Gender
	(*StudentRequest)(nil),  // 1: address.StudentRequest
	(*StudentResponse)(nil), // 2: address.StudentResponse
}
var file_mytest_proto_depIdxs = []int32{
	0, // 0: address.StudentRequest.gender:type_name -> address.Gender
	1, // 1: address.StudentResponse.StudentRequestFields:type_name -> address.StudentRequest
	1, // 2: address.BirthYearService.BirthYear:input_type -> address.StudentRequest
	1, // 3: address.TwoAfterYearAgeService.TwoAfterYearAge:input_type -> address.StudentRequest
	2, // 4: address.BirthYearService.BirthYear:output_type -> address.StudentResponse
	2, // 5: address.TwoAfterYearAgeService.TwoAfterYearAge:output_type -> address.StudentResponse
	4, // [4:6] is the sub-list for method output_type
	2, // [2:4] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_mytest_proto_init() }
func file_mytest_proto_init() {
	if File_mytest_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_mytest_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StudentRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_mytest_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*StudentResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_mytest_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   2,
		},
		GoTypes:           file_mytest_proto_goTypes,
		DependencyIndexes: file_mytest_proto_depIdxs,
		EnumInfos:         file_mytest_proto_enumTypes,
		MessageInfos:      file_mytest_proto_msgTypes,
	}.Build()
	File_mytest_proto = out.File
	file_mytest_proto_rawDesc = nil
	file_mytest_proto_goTypes = nil
	file_mytest_proto_depIdxs = nil
}
