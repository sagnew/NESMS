prev = "";
msg = "";

function write_file (filename, text)
    output = io.open(filename, "w");
    io.output(output);
    io.write(text);
    io.close(output);
end;

function read_file (filename)
    input = io.open(filename, "r");
    io.input(input);
    input_content = io.read();
    io.close(input);

    return input_content;
end;

function handle_input ()
    local address = tonumber(read_file("address.txt"), 16);
    local value = tonumber(read_file("value.txt"), 16);
    local speed = tonumber(read_file("speed.txt"), 16);

    if(address ~= "None" and address ~= nil and value ~= nil) then
        memory.writebyte(address, value);
    end;

    if(speed ~= "None") then
    	emu.speedmode(speed);
    end;
end;

while (true) do
    input_content = read_file("input.txt");

    if(input_content ~= nil) then
        msg = input_content
        emu.message(msg);
    end;

    if(msg ~= prev) then
        prev = msg;
    	handle_input()
    end;

    emu.frameadvance();
end;
