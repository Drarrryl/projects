def decode(message_file) -> str:
  word_dict = {}
  line = message_file.readline()
  while line != '':
    index = 0
    for char in line:
      try:
        if int(char):
          index += 1
      except:
        break
    key = int(line[0:index+1])
    val = line[index+1:]
    word_dict.update({key: val})
    line = message_file.readline()

  level = 1
  step = 2
  decoded_msg = ""
  while level <= len(word_dict):
    decoded_msg += word_dict.get(level)
    level += step
    step += 1
  return decoded_msg

file = open('coding_qual_input.txt', 'r')
print(decode(file))