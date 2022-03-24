using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Text;
using _1;

namespace Test
{
    [TestClass]
    public class LogicOperationsTests
    {
        [TestMethod]
        public void IsTrueANDFalse_False()
        {
            LogicOperations lo = new LogicOperations();

            bool result = lo.AND(true, false);

            Assert.IsFalse(result);
        }

        [TestMethod]
        public void IsTrueORFalse_True()
        {
            LogicOperations lo = new LogicOperations();

            bool result = lo.OR(true, false);

            Assert.IsTrue(result);
        }
    }
}
