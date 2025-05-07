def convert_p6_to_p3(input_path, output_path):
    with open(input_path, 'rb') as f:
        magic_number = f.readline().strip()
        if magic_number != b'P6':
            raise ValueError("This is not a valid P6 PPM file.")

        def read_non_comment_line():
            line = f.readline()
            while line.startswith(b'#') or line.strip() == b'':
                line = f.readline()
            return line.strip()

        size_line = read_non_comment_line()
        while len(size_line.split()) < 2:
            size_line += b' ' + read_non_comment_line()
        width, height = map(int, size_line.split())

        maxval = int(read_non_comment_line())

        pixel_data = f.read()

    with open(output_path, 'w') as f:
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write(f"{maxval}\n")
        for i in range(0, len(pixel_data), 3):
            r = pixel_data[i]
            g = pixel_data[i+1]
            b = pixel_data[i+2]
            f.write(f"{r} {g} {b}\n")

if __name__ == "__main__":
    convert_p6_to_p3("/home/data/colorP6File.ppm", "/home/s32227559/colorP3File.ppm")
