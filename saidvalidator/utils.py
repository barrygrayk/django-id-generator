#
#
#
#
#
# def GetControlDigit (self):
#     d = -1
#     try:
#         a=0
#         for x in range(0,6):
#             a += 2*x
#         b = 0
#         for x in range(0,6):
#             b = b*10+(2*x+1)
#         b *= 2
#         c = 0
#
#
# #     private
# #     int
# #     GetControlDigit()
# #     {
# #         int
# #     d = -1;
# #     try   {int a = 0;
# #     for (int i = 0; i < 6; i++)
# #     {
# #     a += int.Parse(this.ParsedIdString[2 * i].ToString());
# #     }
# #     int b = 0;
# #     for (int i = 0; i < 6; i++)
# #     {
# #     b = b * 10 + int.Parse(this.ParsedIdString[2 * i+1].ToString());
# #     }
# #     b *= 2;
# #     int c = 0;
# #     do
# #     {
# #     c += b % 10;
# #     b = b / 10;
# #     }
# #     while (b > 0);
# #     c += a;
# #     d = 10 - (c % 10);
# #     if (d == 10) d = 0;
# #
# # }
# # catch
# # { / * ignore * /}   return d;
# # }