using System;
using System.IO;
using UnityEngine;

namespace CaineBridge
{
    [Serializable]
    public class SaveData
    {
        public string worldName;
        public string worldMode;
        public string saveTime;
    }

    public class SaveSystem : MonoBehaviour
    {
        public static SaveSystem Instance;

        private string saveFolder;

        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;
                DontDestroyOnLoad(gameObject);

                saveFolder = Path.Combine(
                    Application.persistentDataPath,
                    "CaineSaves"
                );

                Directory.CreateDirectory(saveFolder);
            }
            else
            {
                Destroy(gameObject);
            }
        }

        private string GetPath(string worldName)
        {
            return Path.Combine(
                saveFolder,
                worldName + ".json"
            );
        }

        public void SaveWorld(string worldName)
        {
            SaveData data = new SaveData();

            data.worldName = worldName;
            data.worldMode = WorldManager.Instance.CurrentMode.ToString();
            data.saveTime = DateTime.UtcNow.ToString("o");

            string json = JsonUtility.ToJson(
                data,
                true
            );

            File.WriteAllText(
                GetPath(worldName),
                json
            );

            Debug.Log(
                "[CAINE] Saved world: " + worldName
            );
        }

        public SaveData LoadWorld(string worldName)
        {
            string path = GetPath(worldName);

            if (!File.Exists(path))
            {
                Debug.LogWarning(
                    "[CAINE] Save not found: " + worldName
                );

                return null;
            }

            string json = File.ReadAllText(path);

            SaveData data =
                JsonUtility.FromJson<SaveData>(json);

            Debug.Log(
                "[CAINE] Loaded world: " + worldName
            );

            return data;
        }

        public bool WorldExists(string worldName)
        {
            return File.Exists(
                GetPath(worldName)
            );
        }

        public void DeleteWorld(string worldName)
        {
            string path = GetPath(worldName);

            if (File.Exists(path))
            {
                File.Delete(path);

                Debug.Log(
                    "[CAINE] Deleted world: " + worldName
                );
            }
        }
    }
}