module.exports = async function (context, req) {
    context.log('HTTP trigger function processed a request.');

    // Check if the request body contains JSON data
    if (req.body) {
        // Log the received JSON data
        context.log('Received JSON data:', req.body);

        // Return the JSON data in the response
        context.res = {
            status: 200, // Success status code
            body: {
                message: "Received JSON data",
                data: req.body
            }  // Echo the received JSON data
        };
    } else {
        context.res = {
            status: 400, // Bad request status code
            body: "Please send a request with JSON data."
        };
    }
};