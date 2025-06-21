import os
import re
import sys

def parse_srt(file_path):
    """Extracts subtitle text from an .srt file."""

    try:    
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            content = f.read()

    # Remove timestamps and numbers
    content = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', content)
    
    # Remove extra newlines and spaces
    content = re.sub(r'\n+', '\n', content).strip()
    
    return content

def process_directory(root_dir):
    """Processes the directory and generates markdown output."""
    output = []
    root_name = os.path.basename(root_dir).replace('_', ' ')
    output.append(f"# {root_name}\n")
    
    for subdir in sorted(os.listdir(root_dir)):
        subdir_path = os.path.join(root_dir, subdir)
        
        if os.path.isdir(subdir_path) and '_subtitles' in subdir:
            lesson_name = subdir.replace('_subtitles', '').replace('_', ' ')
            output.append(f"## {lesson_name}\n")
            
            for file in sorted(os.listdir(subdir_path)):
                if file.endswith('.srt'):
                    file_path = os.path.join(subdir_path, file)
                    title = os.path.splitext(file)[0].replace('_', ' ')
                    subtitle_text = parse_srt(file_path)
                    
                    output.append(f"### {title}\n")
                    output.append(f"`{subtitle_text}`\n")
    
    return '\n'.join(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python subs_2_md.py <directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print("Error: Provided path is not a directory.")
        sys.exit(1)
    
    markdown_output = process_directory(root_dir)
    print(markdown_output)
    
    # Save to file
    output_file = os.path.join(root_dir, f"{os.path.basename(root_dir)}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    print(f"Markdown file saved to {output_file}")

if __name__ == "__main__":
    main()
