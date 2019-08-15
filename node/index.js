const AWS = require('aws-sdk')

var comprehendmedical = new AWS.ComprehendMedical({apiVersion: '2018-10-30', region: 'us-east-2'});
var params = {
  Text: '6 yrs old patient suffering from fever' /* required */
};
comprehendmedical.detectEntities(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(JSON.stringify(data));           // successful response
});