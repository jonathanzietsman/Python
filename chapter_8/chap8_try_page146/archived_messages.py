def send_messages(messages, sent_messages):
    """Print each message and move it to the sent_messages list."""
    while messages:
        current_message = messages.pop(0)  # Remove from original list
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)  # Add to sent_messages

messages = ["Hello!", "How are you?", "Let's meet up.", "See you soon."]
sent_messages = []  # Empty list to store sent messages

# Call the function with a copy of the messages list
send_messages(messages[:], sent_messages)  

# Print both lists to verify the original is unchanged
print("\nOriginal messages list:", messages, )  # Should still contain all messages
print("Sent messages list:", sent_messages)  # Should contain sent messages
