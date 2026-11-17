const assert = require("assert");
const _ = require("lodash");
assert.deepStrictEqual(_.chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]]);
assert.strictEqual(_.get({ a: { b: 1 } }, "a.b"), 1);
console.log("lodash", _.VERSION, "ok");
