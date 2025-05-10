

def mapper(line, target_word):
    words = line.strip().split()
    return [1 for word in words if word.lower() == target_word.lower()]

def reducer(mapped_values):
    return sum(mapped_values)

def main():
    file_path ='C:/Users/Omkar/Downloads/freq.txt'  # Replace with your file name
    target_word = input("Enter the word to count: ")

    with open(file_path, 'r') as file:
        mapped_results = []
        for line in file:
            mapped_results.extend(mapper(line, target_word))

    total_count = reducer(mapped_results)
    print(f"Frequency of '{target_word}': {total_count}")

if __name__ == '__main__':
    main()
