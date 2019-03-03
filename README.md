# Twitch-Utils

## Commands

### trecv

```bash
trecv channel

# username This is a message
```

### tsend

```bash
tsend channel message user

# No output
```

## Usage

```bash
# Logging
trecv channel >> channel-logs.txt

# Parsing
trecv channel | awk { print $0 }

# Filtering
trecv channel | grep "filter"

# Automating
for x in {1..5}; do tsend channel message; sleep 30; done
```