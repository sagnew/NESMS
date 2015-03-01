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

while (true) do
    input_content = read_file("input.txt");

    if(input_content ~= nil) then
        msg = input_content
        gui.text(0, 50, msg);
    end;

    emu.frameadvance();
end;
