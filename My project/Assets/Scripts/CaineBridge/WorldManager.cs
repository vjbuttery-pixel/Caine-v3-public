using System.Collections.Generic;
using UnityEngine;

namespace CaineBridge
{
    public class WorldManager : MonoBehaviour
    {
        public static WorldManager Instance;

        public enum WorldMode
        {
            Singleplayer,
            Multiplayer
        }

        public WorldMode CurrentMode = WorldMode.Singleplayer;

        public string CurrentWorldName = "";

        public readonly List<GameObject> AdventureObjects = new();

        private GameObject mainCircus;

        void Awake()
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

        public void RegisterMainCircus(GameObject circus)
        {
            mainCircus = circus;
        }

        public GameObject GetMainCircus()
        {
            return mainCircus;
        }

        public void RegisterAdventureObject(GameObject obj)
        {
            AdventureObjects.Add(obj);
        }

        public void ClearAdventure()
        {
            foreach (GameObject obj in AdventureObjects)
            {
                if (obj != null)
                    Destroy(obj);
            }

            AdventureObjects.Clear();
        }

        public void SetWorld(string worldName, WorldMode mode)
        {
            CurrentWorldName = worldName;
            CurrentMode = mode;

            Debug.Log(
                $"[CAINE] Loaded {worldName} ({mode})"
            );
        }
    }
}