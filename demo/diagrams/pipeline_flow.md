A diagram showing:

[ SQLite DB ]
     |
     v
[ Pipeline Processor ]
     |
     v
[ State Machine ]
     |
     v
[ Updated Lead Status ]

Flow:
1. Fetch pending leads
2. Process each lead
3. Apply state transition
4. Write updated state back to SQLite
