using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using PythonScripts;

public class GameObjTest : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
       PythonManager.RunHelloWorld(); 
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
