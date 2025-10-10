import pandas as pd

# Load CSV file into DataFrame
df = pd.read_csv("./csv/mon-thai-dict.csv")

# Display the DataFrame as a table
#print(df)

word_pairs = list(zip(df.iloc[:, 0], df.iloc[:, 1]))

#print("Mon Words:", mon_words)
#print("Thai Words:", thai_words)
#print("Word Pairs:", word_pairs)

# Process each pair to extract Thai words and pronunciations
for mon_word, thai_word in word_pairs:
    if '[' in thai_word and ']' in thai_word:
        th = thai_word[thai_word.find('[')+1 : thai_word.find(']')]
        thp = f"[{th}]"
        thai_word = thai_word.replace(thp, "")
    # Remove number and the following dot if present
    if thai_word and thai_word[0].isdigit() and thai_word[1] == '.':
        thai_word = thai_word[2:].strip()
    thai_word = thai_word.rstrip('.')
    thai_words_split = [w.strip() for w in thai_word.split(',') if w.strip()]

    thai_word_tuples = []

    # Extract part of speech tags if present
    for w in thai_words_split:
        pos_tags = ["น.", "ส.", "ก.", "ว.", "บุพ.", "สัน.", "อุ.", "ลน.", "ไว."]
        part_of_speech = None
        for tag in pos_tags:
            if tag in w:
                part_of_speech = tag
            word = w.replace(tag, "").strip()
            thai_word_tuples.append((part_of_speech, word))
            break
        else:
            thai_word_tuples.append((None, w))

    #if part_of_speech is None and word is valid then borrow previous pos tag
    #for i in range(len(thai_word_tuples)):
    #    pos, word = thai_word_tuples[i]
    #    if pos is None and word:
    #        # Look backwards for the nearest non-None pos tag
    #        for j in range(i-1, -1, -1):
    #            if thai_word_tuples[j][0] is not None:
    #                pos = thai_word_tuples[j][0]
    #                thai_word_tuples[i] = (pos, word)
    #                break

    # Output the results
    print(f"Mon: {mon_word} | Thai: {thai_word_tuples}")
    print(f"Pronunciation: {th}")



# Save processed data to a new CSV file
output_rows = []
for mon_word, thai_word in word_pairs: 
    if '[' in thai_word and ']' in thai_word:
        th = thai_word[thai_word.find('[')+1 : thai_word.find(']')]
        thp = f"[{th}]"
        thai_word = thai_word.replace(thp, "")
    if thai_word and thai_word[0].isdigit() and thai_word[1] == '.':
        thai_word = thai_word[2:].strip()
    thai_word = thai_word.rstrip('.')
    thai_words_split = [w.strip() for w in thai_word.split(',') if w.strip()]

    for w in thai_words_split:
        pos_tags = ["น.", "ส.", "ก.", "ว.", "บุพ.", "สัน.", "อุ.", "ลน.", "ไว."]
        part_of_speech = None
        for tag in pos_tags:
            if tag in w:
                part_of_speech = tag
                word = w.replace(tag, "").strip()
                output_rows.append((mon_word, th, part_of_speech, word))
                break
        else:
            output_rows.append((mon_word, th, None, w))

    #if part_of_speech is None and word is valid then borrow previous pos tag
    #for i in range(len(thai_word_tuples)):
    #    pos, word = thai_word_tuples[i]
    #    if pos is None and word:
    #        # Look backwards for the nearest non-None pos tag
    #        for j in range(i-1, -1, -1):
    #            if thai_word_tuples[j][0] is not None:
    #                pos = thai_word_tuples[j][0]
    #                thai_word_tuples[i] = (pos, word)
    #                break

output_df = pd.DataFrame(output_rows, columns=['mon', 'pronunciation', 'pos', 'th'])
output_df.to_csv('./csv/mon-thai-dict-processed.csv', index=False, encoding='utf-8-sig')
print("Processed data saved to mon-thai-dict-processed.csv") 
