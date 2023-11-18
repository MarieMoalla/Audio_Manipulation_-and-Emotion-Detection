using UnityEngine;
using UnityEngine.UI;
using System.IO;
using PythonScripts;

public class AudioRecorder : MonoBehaviour
{
    private string audioFilePath;
    private AudioClip recordedAudioClip;

    public Button startRecordingButton;
    public Button stopRecordingButton;
    private int questions = 0;


    void Start()
    {
        startRecordingButton.onClick.AddListener(StartRecording);
        stopRecordingButton.onClick.AddListener(StopRecording);
    }

    void StartRecording()
    {
        // Stop recording if it's already in progress
        Microphone.End(null);

        // Start recording and get the recorded audio clip
        recordedAudioClip = Microphone.Start(null, false, 10, 44100);

        // Generate a unique filename for the audio file
        audioFilePath = Path.Combine(Application.dataPath, "Audios", "question_number_"+questions+".wav").Replace("\\", "/");
        questions++;
    }

    void StopRecording()
    {
        // Stop recording
        Microphone.End(null);

        // Save the recorded audio clip as a WAV file
        SavWav.Save(audioFilePath, recordedAudioClip);

        Debug.Log("Audio recorded and saved at: " + audioFilePath);
    }
}
