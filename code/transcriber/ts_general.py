''' transcriber '''
import whisper

INPUT_FILE = "example.wav"


def main():
    ''' main '''
    model = whisper.load_model("turbo")
    try:
        result = model.transcribe(INPUT_FILE, fp16=False)
    except Exception as trans_error:
        print(f'error is {trans_error}')
        return
    print(result["text"])


if __name__ == "__main__":
    main()
