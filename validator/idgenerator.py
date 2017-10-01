import random


def unique_slug_generator(instance):
    dob = instance.date_of_birth
    # Th code below removes the dashes in th date and removes the 1st 2 digs in the year
    date_to_string = dob.isoformat()[2:].replace("-", "")
    gender = instance.gender
    # The code below is a an if statement short hand If the condition is true the value of the variable
    # will be the second of last value in (false,true)
    gender_val = (random.randint(5000, 9999), random.randint(1000, 4999))[gender == "female"]
    country = instance.country
    country_val = (0, 1)[country == "South Africa"]
    race_val = random.randint(8, 9)
    theID =(date_to_string + str(gender_val) + str(country_val) + str(race_val))
    check_bit =get_control_digit(theID)
    # Checks the range of the check bit and if it between the 0-9 the check bit
    # is converted to a string and added the 12 dig id
    theID+=str((-1, check_bit)[check_bit in range(0,9)])
    return theID


def get_control_digit(id):
    d = -1
    try:
        a =0
        for i in range(0,6):
            a += int(id[2*i])
        b = 0
        for x in range(0,6):
            b = b*10 + int(id[2*x+1])
        b *= 2
        c = 0
        while True:
            c += b % 10
            b = b / 10
            if (b > 0):
                break
        c += a
        d = 10 - (c % 10)
        if(d == 10): d = 0
    except ValueError:
        print("Could not convert to string")
    return d




# private int GetControlDigit()
# {
#   int d = -1;
#   try   {
#       int a = 0;
#     for(int i = 0; i < 6; i++)
#     {
#       a += int.Parse(this.ParsedIdString[2*i].ToString());
#     }
#     int b = 0;
#     for(int i = 0; i < 6; i++)
#     {
#       b = b*10 + int.Parse(this.ParsedIdString[2*i+1].ToString());
#     }
#     b *= 2;
#     int c = 0;
#     do
#     {
#       c += b % 10;
#       b = b / 10;
#     }
#     while(b > 0);
#     c += a;
#     d = 10 - (c % 10);
#     if(d == 10) d = 0;
#   }
#   catch {/*ignore*/}   return d;
