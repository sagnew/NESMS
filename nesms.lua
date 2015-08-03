-- A function to read text files
function read_file (filename)
    input = io.open(filename, "r") -- Open this file with the read flag.
    if input ~= nil then
      io.input(input) -- Set the input that the io library will read from.
      input_content = io.read() -- Read the contents of the file.
      io.close(input) -- Close the file.
    end

    return input_content
end

prev_address = '' -- Variable to keep track of the address.
prev_value = '' -- Variable to keep track of the value.

-- Infinite loop to take control over frame advancing.
while true do
  address = read_file('address.txt')
  value = read_file('value.txt')

  -- Only write to memory if the value has changed.
  if address ~= prev_address or value ~= prev_value then
    hex_address = tonumber(address, 16)
    hex_value = tonumber(address, 16)

    -- Check to see if the entered strings are valid.
    if hex_address == nil or hex_value == nil then
      emu.message('Invalid address or value. Please use valid hex numbers.')
    else
      memory.writebyte(hex_address, hex_value) -- Base 16 for hex values
      emu.message(address..': '..value) -- Print address and value being changed.
    end
  end

  prev_address = address -- Update the address to keep track of changes.
  prev_value = value -- Update the value to keep track of changes.
  emu.frameadvance() -- This essentially tells FCEUX to keep running.
end
