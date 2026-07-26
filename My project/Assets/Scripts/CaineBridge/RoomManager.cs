using System.Collections.Generic;
using UnityEngine;

namespace CaineBridge
{
    public class RoomManager : MonoBehaviour
    {
        public static RoomManager Instance;

        private readonly Dictionary<string, RoomData> rooms = new();

        public const string PublicRoomCode = "PUBLIC";

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

        public RoomData JoinRoom(string roomCode)
        {
            roomCode = roomCode.Trim().ToUpper();

            if (!rooms.ContainsKey(roomCode))
            {
                rooms.Add(roomCode, new RoomData()
                {
                    RoomCode = roomCode,
                    PlayerCount = 0,
                    Loaded = false
                });

                Debug.Log($"[CAINE] Created room {roomCode}");
            }

            RoomData room = rooms[roomCode];

            room.PlayerCount++;

            if (!room.Loaded)
            {
                LoadRoom(room);
            }

            return room;
        }

        public void LeaveRoom(string roomCode)
        {
            roomCode = roomCode.Trim().ToUpper();

            if (!rooms.ContainsKey(roomCode))
                return;

            RoomData room = rooms[roomCode];

            room.PlayerCount = Mathf.Max(0, room.PlayerCount - 1);

            if (room.PlayerCount == 0)
            {
                PauseRoom(room);
            }
        }

        private void LoadRoom(RoomData room)
        {
            room.Loaded = true;

            Debug.Log($"[CAINE] Loading room {room.RoomCode}");

            if (SaveSystem.Instance.WorldExists(room.RoomCode))
            {
                SaveSystem.Instance.LoadWorld(room.RoomCode);
            }
            else
            {
                SaveSystem.Instance.SaveWorld(room.RoomCode);
            }

            WorldSessionManager.Instance.ResumeWorld();
        }

        private void PauseRoom(RoomData room)
        {
            room.Loaded = false;

            Debug.Log($"[CAINE] Pausing room {room.RoomCode}");

            SaveSystem.Instance.SaveWorld(room.RoomCode);

            WorldSessionManager.Instance.PauseWorld();
        }
    }
}