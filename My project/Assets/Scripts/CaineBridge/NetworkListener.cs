using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

namespace CaineBridge
{
    public class NetworkListener : MonoBehaviour
    {
        private TcpClient client;
        private Thread networkThread;

        public string Host = "127.0.0.1";

        public int Port = 5000;

        private volatile bool running;

        void Start()
        {
            running = true;

            networkThread = new Thread(Listen);

            networkThread.Start();
        }

        void OnDestroy()
        {
            running = false;

            client?.Close();

            networkThread?.Join();
        }

        void Listen()
        {
            try
            {
                client = new TcpClient();

                client.Connect(
                    Host,
                    Port
                );

                Debug.Log(
                    "[CAINE] Connected to Python."
                );

                var stream = client.GetStream();

                byte[] buffer = new byte[8192];

                while (running)
                {
                    if (!stream.DataAvailable)
                    {
                        Thread.Sleep(10);
                        continue;
                    }

                    int bytes = stream.Read(
                        buffer,
                        0,
                        buffer.Length
                    );

                    string message =
                        Encoding.UTF8.GetString(
                            buffer,
                            0,
                            bytes
                        );

                    UnityBridge.Instance.QueueCommand(
                        message
                    );
                }
            }
            catch (Exception ex)
            {
                Debug.LogError(
                    "[CAINE] " + ex.Message
                );
            }
        }
    }
}