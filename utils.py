import re
import clipboard
import tiktoken

def read_clipboard():
    text = clipboard.paste()
    return text

def to_clipboard(text):
    clipboard.copy(text)



def count_tokens(messages, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    msg_token_count = 0

    for message in messages:
        msg_token_count += 3 # Add tokens for each message
        for key, value in message.items():
            msg_token_count += len(enc.encode(value)) # Add tokens in set message
            if key == "name":
                msg_token_count += 1 # Add token if name is set
    msg_token_count += 3 # Add tokens to account for ending

    return msg_token_count


def trim_messages(messages, max_tokens):
    
    msg_token_count = 0

    # Check if the system message is about to be deleted
    if count_tokens([messages[0]]) > max_tokens:
        raise Exception("System message is too long to fit within the maximum token limit.")

    while True:
        msg_token_count = count_tokens(messages)
        if msg_token_count <= max_tokens:
            break

        # Remove the oldest non-system message
        for i in range(1, len(messages)):
            if messages[i].get('role') != 'system':
                del messages[i]
                break

    return messages

def main():
    pass


if __name__ == "__main__":
    main()
