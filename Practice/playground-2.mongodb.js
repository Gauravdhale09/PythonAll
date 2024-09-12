

// Select the database to use.
use('Signup');

// Insert a few documents into the sales collection.
db.getCollection('Addition').insertMany(
    [
        {
          "_id": "66e2cf9ed9bf15ea29268169" ,
          "Name": "Gaurav Dhale",
          "E-mail id": "gauravdhale09@gmail.com",
          "phone no.": "+917507216007",
          "Password": "1YVsL2"
        },
        {
          "_id":"66e2cf9ed9bf15ea29268170",
          "Name": "Rajesh Sharma",
          "E-mail id": "rajesh.sharma@example.com",
          "phone no.": "+911234567890",
          "Password": "p@ssw0rd1"
        },
        {
          "_id":"66e2cf9ed9bf15ea29268171",
          "Name": "Priya Mehta",
          "E-mail id": "priya.mehta@example.com",
          "phone no.": "+918765432109",
          "Password": "Qwerty123"
        },
        {
          "_id": "66e2cf9ed9bf15ea29268172",
          "Name": "Ankit Singh",
          "E-mail id": "ankit.singh@example.com",
          "phone no.": "+919876543210",
          "Password": "Ankit$2021"
        },
        {
          "_id": "66e2cf9ed9bf15ea29268173",
          "Name": "Sonal Patel",
          "E-mail id": "sonal.patel@example.com",
          "phone no.": "+911987654321",
          "Password": "Sonal@Patel"
        },
        {
          "_id": "66e2cf9ed9bf15ea29268174" ,
          "Name": "Vikas Gupta",
          "E-mail id": "vikas.gupta@example.com",
          "phone no.": "+919123456789",
          "Password": "Gupta!234"
        },
        {
          "_id": "66e2cf9ed9bf15ea29268175",
          "Name": "Riya Desai",
          "E-mail id": "riya.desai@example.com",
          "phone no.": "+918345678912",
          "Password": "Desai#567"
        },
        {
          "_id":"66e2cf9ed9bf15ea29268176" ,
          "Name": "Amit Verma",
          "E-mail id": "amit.verma@example.com",
          "phone no.": "+918945671234",
          "Password": "AmitV@me2023"
        },
        {
          "_id":"66e2cf9ed9bf15ea29268177",
          "Name": "Kiran Rao",
          "E-mail id": "kiran.rao@example.com",
          "phone no.": "+918756490123",
          "Password": "RaoPass123!"
        },
        {
          "_id": "66e2cf9ed9bf15ea29268178" ,
          "Name": "Neha Kapoor",
          "E-mail id": "neha.kapoor@example.com",
          "phone no.": "+919345612098",
          "Password": "Neh@Kapoor"
        }
      ]
      
);


// Print a message to the output window.
console.log(`Data inserted successfully`);

