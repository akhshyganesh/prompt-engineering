# 💻 Code Generation Use Cases

This directory contains comprehensive examples and templates for using prompt engineering in code generation scenarios. From simple function generation to complex architecture design, these examples demonstrate best practices for AI-assisted programming.

## 🗂️ Use Case Categories

### 🎯 Function & Method Generation
- Single-purpose functions
- Class methods and constructors
- Utility functions
- API endpoints
- Database queries

### 🏗️ Architecture & Design
- System architecture planning
- Database schema design
- API design
- Microservices architecture
- Design pattern implementation

### 🐛 Debugging & Optimization
- Bug identification and fixing
- Performance optimization
- Code refactoring
- Security vulnerability detection
- Code review automation

### 📚 Documentation & Testing
- Code documentation generation
- Unit test generation
- API documentation
- README file creation
- Code comment generation

### 🔄 Translation & Migration
- Language translation (Python to JavaScript, etc.)
- Framework migration
- Legacy code modernization
- Database migration scripts
- Configuration file conversion

## 🚀 Quick Examples

### Basic Function Generation
```
Generate a Python function that validates email addresses using regex.

Requirements:
- Function name: validate_email
- Parameter: email_string (str)
- Return: boolean (True if valid, False if invalid)
- Handle edge cases: None, empty string, whitespace
- Include docstring with examples
- Use robust regex pattern
```

### Class Generation with Methods
```
Create a Python class for managing a shopping cart.

Class requirements:
- Class name: ShoppingCart
- Properties: items (list), total_price (float)
- Methods: add_item(), remove_item(), calculate_total(), clear_cart()
- Each item should have: name, price, quantity
- Include proper error handling
- Add type hints
- Include comprehensive docstrings
```

### API Endpoint Generation
```
Generate a FastAPI endpoint for user authentication.

Endpoint specifications:
- Route: POST /auth/login
- Input: username, password (JSON)
- Output: JWT token or error message
- Include: input validation, password hashing verification, JWT generation
- Error handling: invalid credentials, missing fields, server errors
- Add proper HTTP status codes
- Include OpenAPI documentation
```

## 🎯 Advanced Code Generation Prompts

### 1. **Algorithm Implementation**
```
Implement the QuickSort algorithm in Python with the following specifications:

Requirements:
- Function name: quicksort
- Parameters: arr (list of comparable items), ascending (bool, default=True)
- Return: sorted list (new list, don't modify original)
- Handle edge cases: empty list, single item, duplicate values
- Include time/space complexity analysis in docstring
- Add type hints and comprehensive error handling
- Provide usage examples

Optimization requirements:
- Use random pivot selection to avoid worst-case O(n²)
- Implement iterative version to avoid stack overflow
- Add logging for debugging purposes
- Include performance benchmarking code
```

### 2. **Database Integration**
```
Create a Python class for database operations using SQLAlchemy.

Class specifications:
- Class name: UserRepository
- Database: PostgreSQL
- Table: users (id, username, email, password_hash, created_at, updated_at)

Methods to implement:
- create_user(username, email, password) -> User
- get_user_by_id(user_id) -> Optional[User]
- get_user_by_email(email) -> Optional[User]
- update_user(user_id, **kwargs) -> User
- delete_user(user_id) -> bool
- list_users(limit=10, offset=0) -> List[User]

Requirements:
- Use SQLAlchemy ORM
- Include proper error handling and logging
- Add input validation and sanitization
- Implement connection pooling
- Add type hints and docstrings
- Include transaction management
- Add unit tests for all methods
```

### 3. **Web Scraping Solution**
```
Build a robust web scraper for e-commerce product data.

Scraper specifications:
- Target: Generic e-commerce sites
- Data to extract: product name, price, description, images, ratings
- Output format: JSON and CSV
- Handle: pagination, dynamic content, rate limiting

Technical requirements:
- Use requests-html or Selenium for dynamic content
- Implement retry logic with exponential backoff
- Add user-agent rotation and proxy support
- Include data validation and cleaning
- Create configuration file for different sites
- Add logging and monitoring
- Implement respectful crawling practices

Additional features:
- Price change detection and alerts
- Data visualization dashboard
- Scheduled data collection
- Error recovery and resumption
```

### 4. **Microservice Architecture**
```
Design and implement a microservice for order processing in an e-commerce system.

Service specifications:
- Service name: OrderService
- Framework: FastAPI with async support
- Database: PostgreSQL with Redis caching
- Message queue: RabbitMQ or Apache Kafka

Core functionality:
- Create order from cart
- Process payment (integrate with payment service)
- Manage inventory (integrate with inventory service)
- Send order confirmation (integrate with notification service)
- Handle order status updates
- Generate order reports

Architecture requirements:
- RESTful API with OpenAPI documentation
- Event-driven architecture with message queues
- Circuit breaker pattern for external service calls
- Distributed tracing with OpenTelemetry
- Health checks and metrics collection
- Docker containerization with Docker Compose
- Kubernetes deployment manifests
- Unit and integration tests with 90%+ coverage

Include:
- Error handling and retry mechanisms
- Rate limiting and authentication
- Logging and monitoring setup
- Database migration scripts
- CI/CD pipeline configuration
```

## 🛠️ Code Review and Optimization Prompts

### 1. **Code Review Analysis**
```
Review the following Python code for a data processing pipeline:

[CODE TO REVIEW]

Analyze for:
1. Code quality and readability
2. Performance bottlenecks
3. Security vulnerabilities
4. Error handling completeness
5. Testing coverage gaps
6. Documentation quality
7. Adherence to Python best practices (PEP 8, etc.)

Provide:
- Specific line-by-line feedback
- Refactored code examples
- Performance improvement suggestions
- Security enhancement recommendations
- Test case recommendations
- Documentation improvements

Rate overall code quality (1-10) and justify the rating.
```

### 2. **Performance Optimization**
```
Optimize this Python function for better performance:

[ORIGINAL FUNCTION CODE]

Current performance issues:
- Processing 10,000 records takes 30 seconds
- Memory usage grows linearly with input size
- CPU utilization is only 25% (not using multiple cores)

Optimization goals:
- Reduce processing time by 70%
- Minimize memory footprint
- Utilize multiple CPU cores
- Maintain code readability

Provide:
- Optimized version with explanations
- Performance comparison benchmarks
- Memory usage analysis
- Scalability considerations
- Alternative algorithms if applicable
```

## 🧪 Testing and Documentation Generation

### 1. **Comprehensive Test Suite**
```
Generate a complete test suite for this Python class:

[CLASS CODE]

Test requirements:
- Unit tests for all public methods
- Edge case testing (empty inputs, None values, invalid data)
- Error condition testing
- Integration tests with external dependencies
- Performance tests for critical methods
- Property-based testing where applicable

Framework: pytest with appropriate plugins
Coverage target: 95%+

Include:
- Test fixtures and setup/teardown
- Mock objects for external dependencies
- Parametrized tests for multiple scenarios
- Test data factories
- Performance benchmarks
- Documentation for running tests
```

### 2. **API Documentation Generator**
```
Generate comprehensive API documentation for this FastAPI application:

[API CODE]

Documentation requirements:
- OpenAPI/Swagger specification
- Detailed endpoint descriptions
- Request/response examples
- Error code explanations
- Authentication requirements
- Rate limiting information
- SDK examples in Python, JavaScript, and cURL

Include:
- Interactive API explorer
- Code examples for each endpoint
- SDKs for popular languages
- Postman collection
- Integration guides
- Troubleshooting section
```

## 🔄 Legacy Code Modernization

### 1. **Python 2 to 3 Migration**
```
Migrate this Python 2.7 code to Python 3.9+ with modern best practices:

[LEGACY CODE]

Migration requirements:
- Update syntax and imports
- Replace deprecated libraries
- Add type hints
- Implement modern error handling
- Use f-strings for formatting
- Apply current security practices
- Add comprehensive logging
- Update to modern libraries (requests instead of urllib2, etc.)

Modernization goals:
- Improve performance and memory efficiency
- Enhance code readability and maintainability
- Add proper testing infrastructure
- Implement CI/CD compatibility
- Ensure security compliance
```

### 2. **Monolith to Microservices**
```
Break down this monolithic application into microservices:

[MONOLITH CODE STRUCTURE]

Analysis requirements:
- Identify service boundaries
- Define service interfaces
- Plan data migration strategy
- Design inter-service communication
- Handle distributed transactions

Output:
- Service decomposition plan
- API contracts for each service
- Database splitting strategy
- Deployment architecture
- Migration roadmap with phases
- Risk assessment and mitigation
```

## 🎯 Domain-Specific Code Generation

### 1. **Machine Learning Pipeline**
```
Create a complete machine learning pipeline for fraud detection:

Problem specification:
- Dataset: Credit card transactions
- Features: transaction amount, merchant category, time, location, user history
- Target: binary classification (fraud/legitimate)
- Requirements: real-time inference, 99.5%+ accuracy

Pipeline components:
- Data preprocessing and feature engineering
- Model training with hyperparameter tuning
- Model evaluation and validation
- Model deployment with API endpoint
- Monitoring and alerting system
- A/B testing framework

Technical stack:
- pandas, scikit-learn, XGBoost
- MLflow for experiment tracking
- FastAPI for model serving
- Docker for containerization
- Kubernetes for orchestration
```

### 2. **Blockchain Smart Contract**
```
Develop a Solidity smart contract for a decentralized voting system:

Contract requirements:
- Voter registration with identity verification
- Proposal creation and management
- Secure voting mechanism
- Vote tallying and result publication
- Transparency and auditability

Security features:
- Prevent double voting
- Ensure vote privacy until counting
- Protect against common attacks (reentrancy, overflow, etc.)
- Gas optimization
- Access control mechanisms

Include:
- Comprehensive test suite using Hardhat
- Gas usage optimization
- Security audit checklist
- Deployment scripts for different networks
- Frontend integration examples
```

## 📊 Performance Benchmarking

### Code Performance Comparison
```
Create a performance comparison between different implementations:

Task: Sort 1 million integers
Implementations to compare:
1. Built-in sorted() function
2. Custom quicksort
3. Merge sort
4. Heap sort
5. Radix sort

Comparison metrics:
- Execution time
- Memory usage
- CPU utilization
- Scalability with different input sizes
- Performance with different data distributions

Output format:
- Benchmark results table
- Performance graphs
- Recommendations for different scenarios
- Code examples for each implementation
```

## 🎓 Learning and Best Practices

### Code Generation Best Practices

1. **Be Specific About Requirements**
   - Specify exact function signatures
   - Define input/output formats
   - Include error handling requirements
   - Mention performance constraints

2. **Include Context and Constraints**
   - Programming language and version
   - Framework and library versions
   - Performance requirements
   - Security considerations

3. **Request Documentation and Tests**
   - Always ask for docstrings/comments
   - Request unit tests
   - Include usage examples
   - Ask for error handling

4. **Specify Code Quality Standards**
   - Mention coding standards (PEP 8, etc.)
   - Request type hints
   - Ask for proper variable naming
   - Include logging where appropriate

### Common Pitfalls to Avoid

❌ **Vague Requirements**
```
"Write a function to process data"
```

✅ **Specific Requirements**
```
"Write a Python function that processes CSV files containing user data, validates email addresses, removes duplicates, and returns a pandas DataFrame with clean data"
```

❌ **No Error Handling Mentioned**
```
"Create a database connection function"
```

✅ **Include Error Handling**
```
"Create a database connection function with proper error handling, connection pooling, and retry logic for temporary failures"
```

## 🚀 Advanced Techniques

### Chain-of-Thought for Complex Code
```
Design a distributed caching system step by step:

Step 1: Analyze requirements
- Expected load: 100K requests/second
- Data size: 10GB total cache
- Latency requirement: <5ms
- Consistency: eventual consistency acceptable

Step 2: Choose architecture pattern
- Evaluate options: single-node, master-slave, distributed hash table
- Consider trade-offs: consistency vs availability vs partition tolerance
- Select optimal pattern with justification

Step 3: Design data structures and algorithms
- Cache eviction policy (LRU, LFU, etc.)
- Hashing algorithm for distribution
- Conflict resolution mechanisms
- Replication strategy

Step 4: Implementation planning
- Technology stack selection
- API design
- Monitoring and metrics
- Deployment strategy

Step 5: Create implementation
- Core caching logic
- Network communication
- Configuration management
- Testing strategy

Provide detailed reasoning for each step and final implementation.
```

## 📚 Resources and References

- [Clean Code Principles](https://clean-code-developer.com/)
- [Design Patterns](https://refactoring.guru/design-patterns)
- [Algorithm Complexity Analysis](https://www.bigocheatsheet.com/)
- [Security Best Practices](https://owasp.org/www-project-top-ten/)
- [Testing Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)

---

**Next Steps:**
1. Practice with the basic examples
2. Adapt prompts to your specific tech stack
3. Build a library of tested prompts
4. Contribute your own successful prompts

**Remember:** Great code generation prompts are specific, contextual, and include quality requirements from the start.
