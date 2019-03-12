# twitch-chat-utils

## Commands

### trecv

```bash
trecv channel
```

### tsend

```bash
tsend channel username message
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
for x in {1..5}; do tsend channel username message; sleep 30; done

# Respond
trecv channel | awk '$2 ~ /!command/ { system("tsend channel username message") }'
```
