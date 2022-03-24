using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using _1;

namespace Test
{
    [TestClass]
    public class NWDTests
    {
        [TestMethod]
        public void NWDOf128And96Is32()
        {
            Nwd nwd = new Nwd();

            int result = nwd.NWD(128, 96);

            Assert.AreEqual(32, result);
        }

        [TestMethod]
        public void NWDOf31And72Is1()
        {
            Nwd nwd = new Nwd();

            int result = nwd.NWD(31, 72);

            Assert.AreEqual(1, result);
        }

        [TestMethod]
        public void NWDOf31And0Is31()
        {
            Nwd nwd = new Nwd();

            int result = nwd.NWD(31, 0);

            Assert.AreEqual(31, result);
        }

        [TestMethod]
        public void NWDOf0And73Is73()
        {
            Nwd nwd = new Nwd();

            int result = nwd.NWD(0, 73);

            Assert.AreEqual(73, result);
        }

        [TestMethod]
        public void NWDOf0And0ThrowsException()
        {
            Nwd nwd = new Nwd();

            int result = 0;

            Assert.ThrowsException<ArgumentException>(() => result = nwd.NWD(0, 0));
        }
    }
}
