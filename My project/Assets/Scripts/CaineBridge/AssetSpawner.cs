using UnityEngine;

namespace CaineBridge
{
    public static class AssetSpawner
    {
        public static GameObject Spawn(
            string prefabName,
            Vector3 position,
            Quaternion rotation
        )
        {
            GameObject prefab =
                PrefabRegistry.Instance.GetPrefab(
                    prefabName
                );


            if (prefab == null)
            {
                Debug.LogWarning(
                    "[CAINE] Prefab not found: "
                    + prefabName
                );

                return null;
            }


            GameObject obj =
                Object.Instantiate(
                    prefab,
                    position,
                    rotation
                );


            obj.name = prefabName;


            Debug.Log(
                "[CAINE] Spawned: "
                + prefabName
            );


            return obj;
        }
    }
}