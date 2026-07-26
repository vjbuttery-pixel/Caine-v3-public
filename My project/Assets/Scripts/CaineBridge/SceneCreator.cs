using UnityEngine;

namespace CaineBridge
{
    /// <summary>
    /// Temporary scene creation class.
    /// Later this will build full scenes from
    /// Python-generated data.
    /// </summary>
    public static class SceneCreator
    {
        public static void CreateMainCircus()
        {
            Debug.Log("[CAINE] Creating Main Circus...");

            // Temporary placeholder object
            GameObject circus = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
            circus.name = "Main Circus";

            circus.transform.position = Vector3.zero;
            circus.transform.localScale = new Vector3(20f, 1f, 20f);
        }

        public static void CreateAdventure()
        {
            Debug.Log("[CAINE] Creating Adventure...");

            // Temporary placeholder object
            GameObject adventure = GameObject.CreatePrimitive(PrimitiveType.Cube);
            adventure.name = "Adventure Area";

            adventure.transform.position = new Vector3(50f, 0.5f, 0f);
            adventure.transform.localScale = new Vector3(10f, 1f, 10f);
        }
    }
}