import random
import string

def gen_headers(n=10):
   return [ str("field" + i ) for i in range(n)]

def thin_field_gen():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(random.randint(8,16)))

def thick_field_gen():
   try:
      get_char = unichr
   except NameError:
      get_char = chr

   # Update this to include code point ranges to be sampled
   include_ranges = [
      ( 0x0021, 0x0021 ),
      ( 0x0023, 0x0026 ),
      ( 0x0028, 0x007E ),
      ( 0x00A1, 0x00AC ),
      ( 0x00AE, 0x00FF ),
      ( 0x0100, 0x017F ),
      ( 0x0180, 0x024F ),
      ( 0x2C60, 0x2C7F ),
      ( 0x16A0, 0x16F0 ),
      ( 0x0370, 0x0377 ),
      ( 0x037A, 0x037E ),
      ( 0x0384, 0x038A ),
      ( 0x038C, 0x038C ),
   ]

   alphabet = [
      get_char(code_point) for current_range in include_ranges
         for code_point in range(current_range[0], current_range[1] + 1)
   ]
   return ''.join(random.choice(alphabet) for i in range(random.randint(60,200)))


def record_gen(headers, thin=8, thick=2):
   thin_record = { k:thin_field_gen()   for k in headers[0:thin]}
   thick_record = { k :  thick_field_gen() for k in headers[thin:thick+thin]}
   nones = {k:None for k in headers[thick+thin::]}
   all_kv = dict(thin_record, **thick_record)
   all_kv.update(nones)
   return  all_kv



def gen_schema(headers):
   from fastavro import parse_schema
   schema_headers = [{'name':  header, 'type' : ['string', 'null']}   for header in headers]

   schema = {
      'name': 'testschema',
      'namespace': 'test',
      'type': 'record',
      'fields': schema_headers,
   }
   return parse_schema(schema_headers)
