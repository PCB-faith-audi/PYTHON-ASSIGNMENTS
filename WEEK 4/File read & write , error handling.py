def file_read_write():
    # ask user for filename
    filename = input("power.pdf")

    try:
        # try opening and reading the file
        with open("power.pdf", "rb") as file:
            content = file.read()
            print("content read successfully!")

        # modify content
        modified_content = content.upper()

        # write modified content to a new file
        output_filename = "modified_" + filename
        with open(output_filename, "wb") as file:
            file.write(modified_content)
        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print("❌ Error: File does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# run the function
file_read_write()