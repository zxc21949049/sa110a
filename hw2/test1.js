import * as _ from '../pullAllWith.js'

//import _ from "https://dev.jspm.io/lodash";
var objects = [{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }];
 
var a = _.pullAllWith(objects, function(o) { return o.n; });
console.log(a)
// => 20
// The `_.property` iteratee shorthand.
var b =  _.pullAllWith(objects, 'n');
console.log(b)
// => 20