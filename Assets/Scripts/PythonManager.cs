using UnityEditor.Scripting.Python;
using UnityEditor;
using UnityEngine;

namespace PythonScripts
{
public class PythonManager
{
[MenuItem("Python/HelloWorld")]
    public static void RunHelloWorld()
    {
        PythonRunner.RunFile($"{Application.dataPath}/Scripts/Python Script/HelloWorld.py");
    }
[MenuItem("Python/Part1")]
    public static void RunPart1()
    {
        PythonRunner.RunFile($"{Application.dataPath}/Scripts/Python Script/AudioSegmentation.py");
    }
}
}
