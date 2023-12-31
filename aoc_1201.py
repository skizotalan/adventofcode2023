from aoc_1201_input import input, text_to_num_dict

def get_lines(input): return iter(input.splitlines())

def get_num_from_text(input):
  if input in text_to_num_dict:
    return(text_to_num_dict[input])
  else:
    return(-1)
  

if __name__ == '__main__':
  total = 0

  for line in get_lines(input):
    this_line = line
    num_chars = len(this_line)

    first_num = -1
    last_num = -1
    i = 0
    for char in this_line:
      if char.isnumeric():
        if first_num == -1:
          first_num = char
          last_num = char
        else:
          last_num = char
      else:
        num_text = -1
        # check for 5 character written number
        num_text = get_num_from_text(this_line[i:i+5])
        if num_text == -1:
          # check for 4 character written number
          num_text = get_num_from_text(this_line[i:i+4])
        if num_text == -1:
          # check for 3 character written number
          num_text = get_num_from_text(this_line[i:i+3])
        if num_text != -1:
          if first_num == -1:
            first_num = num_text
            last_num = num_text
          else:
            last_num = num_text
      
      i+=1
    
    print(first_num)
    print(last_num)
    new_num = int(str(first_num) + str(last_num))
    print(f'result: {new_num}')
    
    total = total + new_num

  print(total)
        
      

