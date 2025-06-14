#!/bin/bash

# Prompt Engineering Repository Setup Script
# This script sets up your environment for prompt engineering practice and development

set -e  # Exit on any error

echo "🚀 Setting up Prompt Engineering Repository..."
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# Check if running on supported OS
print_header "🔍 Checking system requirements..."

if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
    PACKAGE_MANAGER="brew"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
    if command -v apt-get &> /dev/null; then
        PACKAGE_MANAGER="apt"
    elif command -v yum &> /dev/null; then
        PACKAGE_MANAGER="yum"
    else
        print_error "Unsupported Linux distribution"
        exit 1
    fi
else
    print_error "Unsupported operating system: $OSTYPE"
    exit 1
fi

print_status "Detected OS: $OS"
print_status "Package manager: $PACKAGE_MANAGER"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check and install dependencies
print_header "📦 Checking and installing dependencies..."

# Check Python
if command_exists python3; then
    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
    print_status "Python 3 found: $PYTHON_VERSION"
else
    print_error "Python 3 is required but not installed"
    if [[ "$OS" == "macOS" ]]; then
        print_status "Installing Python 3 via Homebrew..."
        brew install python
    elif [[ "$PACKAGE_MANAGER" == "apt" ]]; then
        print_status "Installing Python 3 via apt..."
        sudo apt update && sudo apt install -y python3 python3-pip python3-venv
    fi
fi

# Check Node.js
if command_exists node; then
    NODE_VERSION=$(node --version)
    print_status "Node.js found: $NODE_VERSION"
else
    print_warning "Node.js not found. Some features require Node.js."
    echo "Would you like to install Node.js? (y/n)"
    read -r install_node
    if [[ $install_node =~ ^[Yy]$ ]]; then
        if [[ "$OS" == "macOS" ]]; then
            print_status "Installing Node.js via Homebrew..."
            brew install node
        elif [[ "$PACKAGE_MANAGER" == "apt" ]]; then
            print_status "Installing Node.js via apt..."
            curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
            sudo apt-get install -y nodejs
        fi
    fi
fi

# Check Git
if ! command_exists git; then
    print_error "Git is required but not installed"
    if [[ "$OS" == "macOS" ]]; then
        print_status "Installing Git via Homebrew..."
        brew install git
    elif [[ "$PACKAGE_MANAGER" == "apt" ]]; then
        print_status "Installing Git via apt..."
        sudo apt update && sudo apt install -y git
    fi
fi

# Set up Python virtual environment
print_header "🐍 Setting up Python environment..."

cd implementations/python

if [[ ! -d "venv" ]]; then
    print_status "Creating Python virtual environment..."
    python3 -m venv venv
fi

print_status "Activating virtual environment..."
source venv/bin/activate

print_status "Upgrading pip..."
pip install --upgrade pip

print_status "Installing Python dependencies..."
if [[ -f "requirements.txt" ]]; then
    pip install -r requirements.txt
else
    print_warning "requirements.txt not found, installing basic dependencies..."
    pip install openai anthropic python-dotenv pandas numpy jupyter
fi

cd ../../

# Set up Node.js environment (if Node.js is available)
if command_exists node; then
    print_header "📦 Setting up Node.js environment..."
    
    cd rag
    
    if [[ -f "package.json" ]]; then
        print_status "Installing Node.js dependencies..."
        npm install
    else
        print_warning "package.json not found in rag directory"
    fi
    
    cd ../
fi

# Create environment file templates
print_header "⚙️ Setting up configuration files..."

# Python environment file
if [[ ! -f "implementations/python/.env" ]]; then
    print_status "Creating Python .env file..."
    cat > implementations/python/.env << EOF
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API Configuration (optional)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Other API Keys (optional)
GOOGLE_API_KEY=your_google_api_key_here
COHERE_API_KEY=your_cohere_api_key_here

# Application Settings
LOG_LEVEL=INFO
CACHE_ENABLED=true
MAX_TOKENS=2000
TEMPERATURE=0.7

# Database Configuration (if using)
DATABASE_URL=sqlite:///prompt_engineering.db

# Redis Configuration (if using)
REDIS_URL=redis://localhost:6379
EOF
    print_warning "Please edit implementations/python/.env and add your API keys"
fi

# RAG environment file
if [[ ! -f "rag/.env" ]] && [[ -f "rag/sample.env" ]]; then
    print_status "Creating RAG .env file from template..."
    cp rag/sample.env rag/.env
    print_warning "Please edit rag/.env and add your OpenAI API key"
fi

# Create useful directories
print_header "📁 Creating project directories..."

directories=(
    "experiments"
    "saved_prompts"
    "test_results"
    "user_configs"
    "logs"
)

for dir in "${directories[@]}"; do
    if [[ ! -d "$dir" ]]; then
        print_status "Creating directory: $dir"
        mkdir -p "$dir"
    fi
done

# Set up Git hooks (optional)
print_header "🔧 Setting up development tools..."

if [[ -d ".git" ]]; then
    print_status "Setting up Git hooks..."
    
    # Pre-commit hook for Python formatting
    cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Auto-format Python files before commit

if command -v black &> /dev/null; then
    echo "Running black formatter..."
    black implementations/python/ --check --diff
    if [ $? -ne 0 ]; then
        echo "Python files need formatting. Run: black implementations/python/"
        exit 1
    fi
fi

if command -v flake8 &> /dev/null; then
    echo "Running flake8 linter..."
    flake8 implementations/python/ --max-line-length=88
    if [ $? -ne 0 ]; then
        echo "Python files have linting issues. Please fix them."
        exit 1
    fi
fi
EOF
    chmod +x .git/hooks/pre-commit
    print_status "Git pre-commit hook installed"
fi

# Create useful scripts
print_header "📜 Creating utility scripts..."

# Quick start script for Python
cat > implementations/python/quick_start.sh << 'EOF'
#!/bin/bash
# Quick start script for Python prompt engineering

echo "🚀 Starting Python Prompt Engineering Environment..."

# Activate virtual environment
source venv/bin/activate

# Check if .env file exists and has API key
if [[ -f ".env" ]]; then
    if grep -q "your_openai_api_key_here" .env; then
        echo "⚠️  Please add your OpenAI API key to .env file"
    else
        echo "✅ Environment configured"
    fi
else
    echo "❌ .env file not found. Run setup.sh first."
    exit 1
fi

# Run example if requested
if [[ "$1" == "example" ]]; then
    echo "🏃 Running basic example..."
    python examples/basic_prompting.py
elif [[ "$1" == "jupyter" ]]; then
    echo "📓 Starting Jupyter notebook..."
    jupyter notebook
else
    echo "💡 Usage:"
    echo "  ./quick_start.sh example  - Run basic example"
    echo "  ./quick_start.sh jupyter - Start Jupyter notebook"
    echo "  ./quick_start.sh         - Just activate environment"
fi
EOF
chmod +x implementations/python/quick_start.sh

# Quick start script for RAG
if [[ -f "rag/package.json" ]]; then
    cat > rag/quick_start.sh << 'EOF'
#!/bin/bash
# Quick start script for RAG system

echo "🚀 Starting RAG System..."

# Check if .env file exists and has API key
if [[ -f ".env" ]]; then
    if grep -q "your_openai_api_key_here" .env; then
        echo "⚠️  Please add your OpenAI API key to .env file"
        exit 1
    else
        echo "✅ Environment configured"
    fi
else
    echo "❌ .env file not found. Copy sample.env to .env and add your API key."
    exit 1
fi

# Run RAG system with example
echo "🏃 Running RAG example..."
node index.js sample_blog.txt "What is the main topic of this document?"
EOF
    chmod +x rag/quick_start.sh
fi

# Test script
cat > test_setup.sh << 'EOF'
#!/bin/bash
# Test script to verify setup

echo "🧪 Testing Prompt Engineering Setup..."

# Test Python environment
echo "Testing Python environment..."
cd implementations/python
source venv/bin/activate

python -c "
import sys
print(f'Python version: {sys.version}')

try:
    import openai
    print('✅ OpenAI library installed')
except ImportError:
    print('❌ OpenAI library not found')

try:
    import pandas
    print('✅ Pandas installed')
except ImportError:
    print('❌ Pandas not found')

try:
    import dotenv
    print('✅ python-dotenv installed')
except ImportError:
    print('❌ python-dotenv not found')
"

cd ../../

# Test Node.js environment
if command -v node &> /dev/null; then
    echo "Testing Node.js environment..."
    cd rag
    
    if [[ -f "package.json" ]]; then
        node -e "
        console.log('Node.js version:', process.version);
        try {
            require('openai');
            console.log('✅ OpenAI package installed');
        } catch (e) {
            console.log('❌ OpenAI package not found');
        }
        "
    fi
    
    cd ../
fi

echo "🎉 Setup test completed!"
EOF
chmod +x test_setup.sh

# Create documentation
print_header "📖 Creating documentation..."

cat > GETTING_STARTED.md << 'EOF'
# 🚀 Getting Started Guide

## Quick Setup

1. Run the setup script:
   ```bash
   ./setup.sh
   ```

2. Add your API keys:
   ```bash
   # For Python examples
   edit implementations/python/.env
   
   # For RAG system  
   edit rag/.env
   ```

3. Test your setup:
   ```bash
   ./test_setup.sh
   ```

## Running Examples

### Python Examples
```bash
cd implementations/python
./quick_start.sh example
```

### RAG System
```bash
cd rag
./quick_start.sh
```

### Jupyter Notebooks
```bash
cd implementations/python
./quick_start.sh jupyter
```

## Next Steps

- Read the [README.md](README.md) for full documentation
- Check out [tutorials/](tutorials/) for step-by-step guides
- Explore [examples/](examples/) for practical use cases
- Join our community discussions

## Need Help?

- Check the [FAQ](resources/faq.md)
- Review [troubleshooting guide](resources/troubleshooting.md)
- Join our [Discord community](https://discord.gg/prompt-engineering)
- Open an issue on GitHub
EOF

# Final status
print_header "🎉 Setup Complete!"

echo ""
print_status "Your prompt engineering environment is ready!"
echo ""
echo "📋 Next steps:"
echo "  1. Add your API keys to the .env files"
echo "  2. Run: ./test_setup.sh to verify installation"
echo "  3. Try: cd implementations/python && ./quick_start.sh example"
echo "  4. Read: GETTING_STARTED.md for more information"
echo ""
echo "📚 Learning resources:"
echo "  - tutorials/ - Step-by-step guides"
echo "  - examples/ - Practical examples"
echo "  - resources/ - Reference materials"
echo ""
echo "🤝 Community:"
echo "  - GitHub Discussions: https://github.com/akhshyganesh/prompt-engineering/discussions"
echo "  - Documentation: README.md"
echo ""

if [[ ! -f "implementations/python/.env" ]] || grep -q "your_openai_api_key_here" implementations/python/.env 2>/dev/null; then
    print_warning "Don't forget to add your OpenAI API key to implementations/python/.env"
fi

if [[ -f "rag/.env" ]] && grep -q "your_openai_api_key_here" rag/.env 2>/dev/null; then
    print_warning "Don't forget to add your OpenAI API key to rag/.env"
fi

print_status "Setup completed successfully! 🎉"