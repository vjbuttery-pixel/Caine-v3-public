using System.Collections.Generic;
using UnityEngine;

namespace CaineBridge
{
    public class ResidentManager : MonoBehaviour
    {
        public static ResidentManager Instance;

        private readonly Dictionary<string, ResidentData> residents = new();

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

        public void RegisterResident(ResidentData resident)
        {
            if (resident == null)
                return;

            residents[resident.Id] = resident;

            Debug.Log($"[CAINE] Resident registered: {resident.Name}");
        }

        public ResidentData GetResident(string id)
        {
            residents.TryGetValue(id, out ResidentData resident);
            return resident;
        }

        public IEnumerable<ResidentData> GetAllResidents()
        {
            return residents.Values;
        }

        public int ResidentCount()
        {
            return residents.Count;
        }
    }
}