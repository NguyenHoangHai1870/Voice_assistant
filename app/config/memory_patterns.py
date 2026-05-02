MEMORY_RULES = [
    {
        "field": "favorite_color",
        "patterns": [
            r"(?:tôi thích màu|màu yêu thích của tôi là)\s+(.+)"
        ],
        "template": "Đã ghi nhớ màu yêu thích của bạn là {}."
    },
    {
        "field": "favorite_food",
        "patterns": [
            r"(?:tôi thích ăn|món yêu thích của tôi là)\s+(.+)"
        ],
        "template": "Đã ghi nhớ món ăn yêu thích của bạn là {}."
    },
    {
        "field": "favorite_drink",
        "patterns": [
            r"(?:tôi thích uống|đồ uống yêu thích của tôi là)\s+(.+)"
        ],
        "template": "Đã ghi nhớ đồ uống yêu thích của bạn là {}."
    },
    {
        "field": "company",
        "patterns": [
            r"(?:tôi làm ở|mình làm ở|công ty của tôi là)\s+(.+)"
        ],
        "template": "Đã ghi nhớ công ty của bạn là {}."
    },
    {
        "field": "name",
        "patterns": [
            r"(?:tôi tên|mình tên|tên tôi là)\s+([^\?]+)$"
        ],
        "template": "Đã ghi nhớ tên của bạn là {}."
    },
    {
        "field": "age",
        "patterns": [
            r"(?:tôi|mình)\s+(\d+)\s+tuổi"
        ],
        "template": "Đã ghi nhớ bạn {} tuổi."
    },
    {
        "field": "hometown",
        "patterns": [
            r"(?:tôi quê ở|mình quê ở|quê tôi là|quê tôi ở)\s+(.+)"
        ],
        "template": "Đã ghi nhớ quê của bạn là {}."
    },
    {
        "field": "location",
        "patterns": [
            r"(?:tôi sống ở|mình sống ở|tôi ở|mình ở)\s+(.+)"
        ],
        "template": "Đã ghi nhớ nơi ở của bạn là {}."
    },
    {
        "field": "education",
        "patterns": [
            r"(?:tôi học ở|mình học ở|tôi học tại|mình học tại)\s+(.+)"
        ],
        "template": "Đã ghi nhớ bạn học tại {}."
    },
    {
        "field": "major",
        "patterns": [
            r"(?:tôi học ngành|mình học ngành|ngành của tôi là)\s+(.+)"
        ],
        "template": "Đã ghi nhớ ngành học của bạn là {}."
    },
    {
        "field": "occupation",
        "patterns": [
            r"(?:tôi làm nghề|mình làm nghề|nghề của tôi là)\s+(.+)"
        ],
        "template": "Đã ghi nhớ nghề nghiệp của bạn là {}."
    },
    {
        "field": "hobbies",
        "patterns": [
            r"(?:tôi thích|mình thích)\s+([a-zA-ZÀ-ỹ0-9 ]{2,30})$"
        ],
        "template": "Đã ghi nhớ sở thích của bạn là {}."
    },
]

PROFILE_QUERY_PATTERNS = [
    {
        "field": "name",
        "patterns": [
            r".*tên.*tôi.*gì.*",
            r".*tôi.*tên.*gì.*"
        ],
        "template": "Bạn tên là {}."
    },

    {
        "field": "age",
        "patterns": [
            r".*tôi.*bao nhiêu tuổi.*",
            r".*tuổi.*tôi.*bao nhiêu.*"
        ],
        "template": "Bạn {} tuổi."
    },

    {
        "field": "hometown",
        "patterns": [
            r".*quê.*tôi.*ở đâu.*",
            r".*tôi.*quê.*ở đâu.*"
        ],
        "template": "Bạn quê ở {}."
    },

    {
        "field": "location",
        "patterns": [
            r".*tôi.*sống.*ở đâu.*",
            r".*tôi.*đang.*ở đâu.*"
        ],
        "template": "Bạn đang sống ở {}."
    },

    {
        "field": "education",
        "patterns": [
            r".*tôi.*học.*ở đâu.*",
            r".*tôi.*học.*trường.*nào.*"
        ],
        "template": "Bạn học tại {}."
    },

    {
        "field": "major",
        "patterns": [
            r".*tôi.*học.*ngành.*gì.*",
            r".*ngành.*của.*tôi.*là.*gì.*"
        ],
        "template": "Bạn học ngành {}."
    },

    {
        "field": "occupation",
        "patterns": [
            r".*tôi.*làm.*nghề.*gì.*",
            r".*nghề.*của.*tôi.*là.*gì.*"
        ],
        "template": "Bạn làm {}."
    },

    {
        "field": "company",
        "patterns": [
            r".*tôi.*làm.*ở đâu.*",
            r".*tôi.*làm.*công ty.*nào.*"
        ],
        "template": "Bạn làm tại {}."
    },

    {
        "field": "hobbies",
        "patterns": [
            r".*tôi.*thích.*gì.*",
            r".*sở thích.*của.*tôi.*là.*gì.*"
        ],
        "template": "Bạn thích {}."
    },

    {
        "field": "favorite_color",
        "patterns": [
            r".*màu.*yêu thích.*của.*tôi.*là.*gì.*",
            r".*tôi.*thích.*màu.*gì.*"
        ],
        "template": "Màu yêu thích của bạn là {}."
    },

    {
        "field": "favorite_food",
        "patterns": [
            r".*món.*ăn.*yêu thích.*của.*tôi.*là.*gì.*",
            r".*tôi.*thích.*ăn.*gì.*"
        ],
        "template": "Món ăn yêu thích của bạn là {}."
    },

    {
        "field": "favorite_drink",
        "patterns": [
            r".*đồ uống.*yêu thích.*của.*tôi.*là.*gì.*",
            r".*tôi.*thích.*uống.*gì.*"
        ],
        "template": "Đồ uống yêu thích của bạn là {}."
    },

    {
        "field": "relationship_status",
        "patterns": [
            r".*tình trạng.*quan hệ.*của.*tôi.*",
            r".*tôi.*có.*người yêu.*chưa.*"
        ],
        "template": "Bạn hiện {}."
    },

    {
        "field": "birthday",
        "patterns": [
            r".*sinh nhật.*tôi.*khi nào.*",
            r".*tôi.*sinh.*ngày.*nào.*"
        ],
        "template": "Sinh nhật của bạn là {}."
    },
]