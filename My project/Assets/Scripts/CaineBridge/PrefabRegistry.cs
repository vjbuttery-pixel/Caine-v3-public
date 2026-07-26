using System.Collections.Generic;
using UnityEngine;

namespace CaineBridge
{
    public class PrefabRegistry : MonoBehaviour
    {
        public static PrefabRegistry Instance;

        [SerializeField]
        private List<GameObject> prefabs = new();

        private readonly Dictionary<string, GameObject> lookup = new();

        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;
                DontDestroyOnLoad(gameObject);

                BuildLookup();
            }
            else
            {
                Destroy(gameObject);
            }
        }

        private void BuildLookup()
        {
            lookup.Clear();

            foreach (GameObject prefab in prefabs)
            {
                if (prefab == null)
                    continue;

                lookup[prefab.name] = prefab;
            }

            Debug.Log($"[CAINE] Loaded {lookup.Count} prefabs.");
        }

        public GameObject GetPrefab(string name)
        {
            lookup.TryGetValue(name, out GameObject prefab);
            return prefab;
        }

        public void RegisterPrefab(GameObject prefab)
        {
            if (prefab == null)
                return;

            lookup[prefab.name] = prefab;

            if (!prefabs.Contains(prefab))
                prefabs.Add(prefab);
        }
    }
}