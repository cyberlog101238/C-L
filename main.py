import base64, codecs
magic = 'aW1wb3J0IG9zDQppbXBvcnQgcmFuZG9tDQppbXBvcnQgd2ViYnJvd3Nlcg0KZnJvbSB0aW1lIGltcG9ydCBzbGVlcA0KDQp0cnk6DQogICAgaW1wb3J0IHJlcXVlc3RzDQpleGNlcHQgSW1wb3J0RXJyb3I6DQogICAgb3Muc3lzdGVtKCdwaXAgaW5zdGFsbCByZXF1ZXN0cycpDQogICAgaW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgdXJsbGliLnJlcXVlc3QNCmltcG9ydCB1cmxsaWIucGFyc2UNCmRlZiBpbnRlcm5ldCgpOg0KICAgIHRyeToNCiAgICAgICAgdXJsbGliLnJlcXVlc3QudXJsb3BlbignaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbScpDQogICAgZXhjZXB0IEV4Y2VwdGlvbjoNCiAgICAgICAgcHJpbnQoIllvdSBhcmUgbm90IGNvbm5lY3RlZCBUbyBJbnRlcm5ldCEhISIpDQogICAgICAgIHByaW50KCJcdFBsZWFzZSBDb25uZWN0IFRvIEludGVybmV0IFRvIENvbnRpbnVlLi4uXG4iKQ0KICAgICAgICBpbnB1dCgnRXhpdGluZy4uLi5cbiBQcmVzcyBFbnRlciBUbyBDb250aW51ZS4uLi4nKQ0KICAgICAgICBleGl0KCkNCnJlZCA9ICdcMDMzWzE7MzFtJw0KZ3JlZW4gPSAnXDAzM1sxOzMybScNCnllbGxvdyA9ICdcMDMzWzE7MzNtJw0KYmx1ZSA9ICdcMDMzWzE7MzRtJw0KdmlvID0gJ1wwMzNbMTszNW0nDQpub24gPSAnXDAzM1sxOzBtJw0KZGVmIGNscigpOg0KICAgIGlmIG9zLm5hbWUgPT0gJ250JzoNCiAgICAgICAgb3Muc3lzdGVtKCdjbHMnKQ0KICAgIGVsc2U6DQogICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KZGVmIGxnbygpOg0KDQogICAgY29sb3JzID0gWydcMDMzWzE7MzFtJywgJ1wwMzNbMTszMm0nLCAnXDAzM1sxOzMzbScsICdcMDMzWzE7MzRtJywgJ1wwMzNbMTszNW0nLCAnXDAzM1sxOzM2bSddDQogICAgVyA9ICdcMDMzWzBtJw0KDQogICAgZGVmIGNscigpOg0KICAgICAgICBpZiBvcy5uYW1lID09ICdudCc6DQogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NscycpDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykNCg0KICAgIGRlZiBsb2dvKCk6DQogICAgICAgIGNscigpDQogICAgICAgIHNsZWVwKDEpDQogICAgICAgIGxnID0gIiIiXDAzM1sxOzM0bQ0KICAgICAgICAgICAgICAuODg4ODg4ODg4LiAgICAgICAgICAgICAgIDg4OCAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgMDAwMCAgICAwMDAwICAgICAgICAgICAgICAwMDAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgODg4ICAgICAgODg4ICAgICAgICAgICAgICA4ODgNCiAgICAgICAgICAgICAgODg4ICAgICAgICAgICBSODg4ODg4OFIgICA4ODggICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgIDAwMCAgICAgICAgICAgUjg4ODg4ODhSICAgMDAwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICA4ODggICAgIDAwMCAgICAgICAgICAgICAgIDg4OCAgICAgICAgICA4OCAgDQogICAgICAgICAgICAgIDAwMDAgICAwMDAwICAgICAgICAgICAgICAgMDAwMCAgICAgICAgMDAwICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgIjAwMDAwMDAwMCIgICAgICAgICAgICAgICA4ODg4ODg4ODg4ODg4OCAgICAgDQogICAgICAgX'
love = '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'
god = 'Nsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9DeWJlci1sb2cvQy1MX3VwZGF0ZXInKQ0KICAgICAgICBzbGVlcCgwLjcpDQogICAgICAgIG9zLnN5c3RlbSgnY2QgJEhPTUUgJiYgY2QgQy1MX3VwZGF0ZXInKQ0KICAgIGVsc2U6DQogICAgICAgIGxnbygpDQogICAgICAgIHByaW50KHJlZCArICJcbjo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6OiIpDQogICAgICAgIHByaW50KGdyZWVuICsgIlxuXHRcdEMtTCBpcyB1cGRhdGVkLiIpDQogICAgICAgIHNsZWVwKDIpDQogICAgICAgIGNscigpDQp1cGRhdGUoKQ0KZGVmIGJhbm5lcigpOg0KICAgIGNvbG9ycyA9IFsnXDAzM1sxOzMxbScsICdcMDMzWzE7MzJtJywgJ1wwMzNbMTszM20nLCAnXDAzM1sxOzM0bScsICdcMDMzWzE7MzVtJywgJ1wwMzNbMTszNm0nXQ0KICAgIFcgPSAnXDAzM1swbScNCg0KICAgIGRlZiBjbHIoKToNCiAgICAgICAgaWYgb3MubmFtZSA9PSAnbnQnOg0KICAgICAgICAgICAgb3Muc3lzdGVtKCdjbHMnKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpDQoNCiAgICBjbHIoKQ0KICAgIGxvZ28gPSAiIiIiIA0KICAuODg4ODg4ODg4LiAgICAgICAgICAgICAgIDg4OCAgICAgICAgICAgICAgICAgICAgICAgICANCiAgMDAwMCAgICAwMDAwICAgICAgICAgICAgICAwMDAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgODg4ICAgICAgODg4ICAgICAgICAgICAgICA4ODgNCiAgODg4ICAgICAgICAgICBSODg4ODg4OFIgICA4ODggICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogIDAwMCAgICAgICAgICAgUjg4ODg4ODhSICAgMDAwICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KICA4ODggICAgIDAwMCAgICAgICAgICAgICAgIDg4OCAgICAgICAgICA4OCAgDQogIDAwMDAgICAwMDAwICAgICAgICAgICAgICAgMDAwMCAgICAgICAgMDAwICAgICAgICAgICAgICAgICAgICANCiAgIjAwMDAwMDAwMCIgICAgICAgICAgICAgICA4ODg4ODg4ODg4ODg4OCAgICAgDQoNCiAgICAgIFwwMzNbMTszNG0gICAgICAgIERldmVsb3BlZCBCeSA6XDAzM1sxOzM0bSBBbCBKYWJpciAgICIiIg0KICAgIHByaW50KHJhbmRvbS5jaG9pY2UoY29sb3JzKSArIGxvZ28gKyBXKQ0KICAgIHByaW50KCJcbiIpDQpkZWYgcnVuKCk6DQogICAgZSA9ICIiDQogICAgYmFubmVyKCkNCiAgICBwcmludChyZWQgKyBlKQ0KICAgIHByaW50KHZpbyArICJcblxuXG49PT5TZWxlY3QgYSBvcHRpb24gZnJvbSBiZWxvdyIpDQogICAgcHJpbnQoeWVsbG93ICsgIlxuXG4xLiBCRCBTbXMgQm9tYmVyIg0KICAgICAgICAgICAgICAgICAgICJcbjIuIEUtbWFpbCBCb21iZXIiDQogICAgICAgICAgICAgICAgICAgIlxuMy4gQy1MIEVuY29kZXIiDQogICAgICAgICAgICAgICAgICAgIlxuNC4gQ29udGFjdCIpDQogICAgY2hvb3NlID0gc3RyKGlucHV0KGJsdWUgKyAiW15dIEVudGVyIGEgb3B0aW9uOiAiK3JlZCkpDQogICAgaWYgY2hvb3NlID09ICcxJzoNCiAgICAgICAgb3Muc3lzdGVtKCdweXRob24gc2JvbWIucHknKQ0KICAgIGVsaWYgY2hvb3NlID09ICcyJzoNCiAgICAgICAgb3Muc3lzdGVtKCdweXRob24gZWJvbWIucHknKQ0KICAgIGVsaWYgY2hvb3N'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
