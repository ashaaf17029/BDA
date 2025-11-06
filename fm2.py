import hashlib

# Function to count trailing zeros in binary
def count_trailing_zeros(num):
    return len(bin(num)) - len(bin(num).rstrip('0'))

# Simple hash function for numeric input
def hash_value(x):
    h = hashlib.sha1(str(x).encode()).hexdigest()
    return int(h[:8], 16)   # Take first 8 hex digits

# Flajolet-Martin algorithm
def flajolet_martin(stream):
    R = 0
    for num in stream:
        hv = hash_value(num)
        r = count_trailing_zeros(hv)
        R = max(R, r)
    return 2 ** R   # Estimated distinct elements

# ---------------------- DRIVER CODE ----------------------
data_stream = [10, 20, 10, 30, 40, 20, 50, 60, 70, 30, 80]

print("Data Stream:", data_stream)
print("True Unique Elements:", len(set(data_stream)))
print("Estimated Unique Elements (Flajolet-Martin):", flajolet_martin(data_stream))

// Step 1: Start Mongo Shell
mongosh

// Step 2: Show all databases
show dbs

// Step 3: Use or create database
use learn

// Step 4: Show databases again
show dbs

// Step 5: Create collection
db.createCollection("emp")

// Step 6: Insert one document
db.emp.insertOne({empid:1, name:"Abhinav", salary:100000})

// Step 7: Insert multiple documents
db.emp.insertMany([
  {empid:2, name:"Hardik", salary:200000},
  {empid:3, name:"Ashaaf", salary:300000}
])

// Step 8: Display all documents
db.emp.find()

// Step 9: Find document by name
db.emp.find({name:"Ashaaf"})

// Step 10: Find document by empid
db.emp.find({empid:2})

// Step 11: Update one document
db.emp.updateOne(
  {name:"Hardik"},
  {$set:{salary:750000, empid:4}}
)

// Step 12: Verify update
db.emp.find({empid:4})

// Step 13: Update another document
db.emp.updateOne(
  {name:"Abhinav"},
  {$set:{salary:750000}}
)

// Step 14: Update multiple documents
db.emp.updateMany(
  {salary:750000},
  {$set:{salary:700000}}
)

// Step 15: Display updated documents
db.emp.find()

// Step 16: Delete one document
db.emp.deleteOne({name:"Ashaaf"})

// Step 17: Verify deletion
db.emp.find()

// Step 18: Drop collection
db.emp.drop()

// Step 19: Drop database
db.dropDatabase()
