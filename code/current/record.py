''' Sound recorder using sounddevice '''
import sounddevice
from scipy.io.wavfile import write

SAMPLE_RATE = 44100
OUTPUT_FILENAME = 'Z://Store//output.wav'


def main():
    ''' Main function '''
    print('Recording...')
    recording = sounddevice.rec(int(5 * SAMPLE_RATE),
                                samplerate=SAMPLE_RATE,
                                channels=2)
    sounddevice.wait()
    print('Done recording.')
    write(OUTPUT_FILENAME, SAMPLE_RATE, recording)


if __name__ == '__main__':
    main()
