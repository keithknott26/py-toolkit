def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output