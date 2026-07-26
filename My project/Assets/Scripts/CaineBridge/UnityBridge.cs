using System;
using System.Collections.Generic;
using UnityEngine;

namespace CaineBridge
{
    /// <summary>
    /// Main entry point for commands coming from Python.
    /// </summary>
    public class UnityBridge : MonoBehaviour
    {
        public static UnityBridge Instance;

        private readonly Queue<string> commandQueue = new();

        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;
                DontDestroyOnLoad(gameObject);
            }
            else
            {
                Destroy(gameObject);
            }
        }

        public void QueueCommand(string command)
        {
            commandQueue.Enqueue(command);
        }

        private void Update()
        {
            while (commandQueue.Count > 0)
            {
                string command = commandQueue.Dequeue();

                Debug.Log($"[CAINE] Processing: {command}");

                CommandProcessor.Process(command);
            }
        }
    }
}