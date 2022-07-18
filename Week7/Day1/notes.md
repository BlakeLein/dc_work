# Node.js

- Node.js, or Node for short, is an open-source, server-side JavaScript runtime environment. You can use Node.js to run JavaScript applications and code in many places outside of a browser, such as on a server.
- Things you can make with Node JS
  -HTTP web servers
  -Microservices or serverless API backends
  -Drivers for database access and querying
  -Interactive command-line interfaces
  -Desktop applications
  -Real-time Internet of Things (IoT) client and server libraries
  -Plug-ins for desktop applications
  -Shell scripts for file manipulation or network access
  -Machine learning libraries and models

## package.json Scripts

- A set of actions that can be run with your project.
- These go in the "script" section of the json package.
- These four scripts are expected by the dev community: start, build, test, and lint.
  - Start: Invokes the node command with the entry file as an argument. An example might be node ./src/index.js. This action invokes the node command and uses the entry file index.js.
  - Build: Describes how to build your project. The build process should produce something that you can ship. For example, a build command could run a TypeScript compiler to produce the JavaScript version of the project that you want to ship.
  - Test: Runs the tests for your project. If you're using a third-party test library, the command should invoke the library's executable file.
  - Lint: Invokes a linter program like ESLint. Linting finds inconsistencies in code. A linter usually offers a way to correct inconsistencies as well. Having consistent code can greatly increase readability, which speeds up the development of features and additions to the code.
- You can invoke the tests with "npm run (script name)"
- With "start" and "test", you can omit the word "run"

## Node Packages

- A dependency is a third-party library, a piece of reusable code that accomplishes something and can be added to your application. The third-party library is something your application depends on to function, hence the word dependency.
- Typing 'npm -help' will show all the commands you can use with the npm keyword. There are four categories:
  1. Managing Dependencies
  2. Running Scripts
  3. Configure the environment
  4. Author and Publish Packages
- Include the -g to install a package globally
