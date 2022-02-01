CREATE TABLE "classes_cvs" (
	"class_name"	TEXT NOT NULL,
	"class_description"	TEXT NOT NULL,
	"class_code"	TEXT NOT NULL UNIQUE,
	"class_admin"	TEXT NOT NULL,
	"class_students"	TEXT DEFAULT '[]',
	PRIMARY KEY("class_code")
);