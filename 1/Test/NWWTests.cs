using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Text;
using _1;

namespace Test
{
    [TestClass]
    public class NWWTests
    { 
        [TestMethod]
        public void NWWOf128And96Is384()
        {
            Nww nww = new Nww();

            int result = nww.NWW(128, 96);

            Assert.AreEqual(384, result);
        }

        [TestMethod]
        public void NWWOf1And251Is251()
        {
            Nww nww = new Nww();

            int result = nww.NWW(1, 251);

            Assert.AreEqual(251, result);
        }

        [TestMethod]
        public void NWWOf0And54Is0()
        {
            Nww nww = new Nww();

            int result = nww.NWW(0, 54);

            Assert.AreEqual(0, result);
        }

        [TestMethod]
        public void NWWOf73And0Is0()
        {
            Nww nww = new Nww();

            int result = nww.NWW(73, 0);

            Assert.AreEqual(0, result);
        }

        [TestMethod]
        public void NWWOf0And0ThrowsArgumentException()
        {
            Nww nww = new Nww();

            int result = 0;

            Assert.ThrowsException<ArgumentException>(() => result = nww.NWW(0, 0));
        }
    }
}
