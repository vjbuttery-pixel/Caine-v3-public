using System;
using System.Collections.Generic;

namespace CaineBridge
{
    [Serializable]
    public class CaineCommand
    {
        public string id;

        public string type;

        public CommandPayload payload;
    }


    [Serializable]
    public class CommandPayload
    {
        public string prefab;

        public string name;

        public string world;

        public string sceneType;


        public float[] position;

        public float[] rotation;


        public string data;
    }
}