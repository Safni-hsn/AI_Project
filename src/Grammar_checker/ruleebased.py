from indicnlp.tokenize import indic_tokenize

# Rule 1: Subject-Verb Agreement Rules (with contextual verbs)
subject_verb_rules = {
    "அவன்": ["பேசுகிறான்", "பாடுகிறான்", "செல்கிறான்"],
    "அவள்": ["பேசுகிறாள்", "பாடுகிறாள்", "செலுகிறாள்"],
    "நான்": ["பேசுகிறேன்", "பாடுகிறேன்", "செலுகிறேன்"],
    "அவர்கள்": ["பேசுகிறார்கள்", "பாடுகிறார்கள்", "செல்கிறார்கள்"]
}

# Rule 2: Valid Tamil Case Markers
valid_case_markers = ["க்கு", "இல்", "அது", "உடன்", "ஆல்"]


def subject_verb_agreement(text):
    errors = []
    corrected_tokens = []
    tokens = indic_tokenize.trivial_tokenize(text)  # Tokenize the text
    i = 0
    while i < len(tokens) - 1:
        token = tokens[i]
        next_token = tokens[i + 1]
        if token in subject_verb_rules:
            if next_token not in subject_verb_rules[token]:
                errors.append(f"Error: '{token} {next_token}' violates subject-verb agreement")
                base_verb = next_token[:-3]
                corrected_verb = next(
                    (verb for verb in subject_verb_rules[token] if verb.startswith(base_verb)),
                    next_token
                )
                corrected_tokens.append(token)
                corrected_tokens.append(corrected_verb)
                i += 2  #
                continue
        corrected_tokens.append(token)
        i += 1
    if i == len(tokens) - 1:
        corrected_tokens.append(tokens[-1])
    return errors, " ".join(corrected_tokens)

def case_marker_check(text):
    errors = []
    corrected_tokens = []
    tokens = indic_tokenize.trivial_tokenize(text)
    for token in tokens:
        if not any(token.endswith(marker) for marker in valid_case_markers) and len(token) > 2:
            errors.append(f"Error: '{token}' does not have a valid case marker")
            corrected_tokens.append(f"{token}க்கு")
        else:
            corrected_tokens.append(token)
    return errors, " ".join(corrected_tokens)


def rule_based_grammar_check(text):

    sva_errors, sva_corrected_text = subject_verb_agreement(text)

    case_marker_errors, case_corrected_text = case_marker_check(sva_corrected_text)

    final_corrected_text = sva_corrected_text if sva_errors else case_corrected_text

    all_errors = sva_errors + case_marker_errors
    return all_errors, final_corrected_text





tamil_text = "அவன் செல்கிறாள்."
errors, corrected_text = rule_based_grammar_check(tamil_text)

print("Grammar Errors Detected:")
if errors:
    for error in errors:
        print(error)
else:
    print("No errors detected!")

print("\nCorrected Text:")
print(corrected_text)
