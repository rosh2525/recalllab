"""Original, reviewed RecallLab course material; no private course files included."""
VERSION = '2026.10.1'
MODULE_ID = 'marginal-thinking'
CONCEPTS = [
 ('marginal','Marginal thinking','Interpret a derivative as a local rate of change.','If total cost is C(q), marginal cost is C′(q). It measures the instantaneous rate at which total cost changes with output. Its units are currency per unit of output. C′(q) approximates the cost of one extra unit; C(q+1)−C(q) is the exact discrete change.'),
 ('average','Average vs. marginal','Separate a level, an average, and a rate.','Total cost is C(q). Average cost is C(q)/q for q>0. Marginal cost is C′(q). Fixed cost changes total and average cost but its derivative is zero.'),
 ('power','The power rule','Differentiate polynomial cost and revenue functions.','For a constant a and positive integer n, d(aqⁿ)/dq = anqⁿ⁻¹. Derivatives add term by term. A constant has derivative zero.'),
 ('constant','Fixed costs','Understand what disappears under differentiation.','A cost that does not depend on output has derivative zero. This does not make fixed cost irrelevant to profit levels or entry decisions; it makes its marginal contribution zero.'),
 ('product','The product rule','Keep both terms when differentiating a product.','For differentiable u and v, (uv)′ = u′v + uv′. When revenue is p(q)q, marginal revenue is p(q) + qp′(q), because price may depend on quantity.'),
 ('chain','The chain rule','Track inner and outer changes.','For f(g(q)), the derivative is f′(g(q))g′(q). For (aq+b)ⁿ it is na(aq+b)ⁿ⁻¹.'),
 ('profit','Profit at the margin','Connect marginal revenue and marginal cost.','Profit is π(q)=R(q)−C(q), so π′(q)=MR(q)−MC(q). At an interior differentiable optimum, π′(q)=0 is necessary, implying MR=MC. Additional checks determine whether the point is a maximum.'),
 ('stationary','Stationary is not optimal','Treat the first-order condition as a candidate test.','A stationary point satisfies f′(q)=0. It may be a local maximum, local minimum, or neither. For f(q)=(q−2)³, f′(2)=0 but the function increases through q=2; this is not a local maximum or minimum.'),
 ('second','Second-order conditions','Distinguish local maxima and minima.','At an interior stationary point, f″(q)<0 is sufficient for a strict local maximum and f″(q)>0 for a strict local minimum. If f″(q)=0, this test is inconclusive. Local conditions alone do not establish a global maximum.'),
 ('boundary','Feasible boundaries','Compare candidates with endpoints.','For a continuous function on a closed interval, evaluate both endpoints and all interior critical points, including points where the derivative does not exist. The largest value is a global maximum on that interval.'),
 ('elasticity','Elasticity','Measure proportional rather than absolute response.','For a differentiable quantity function Q(p), point price elasticity is Q′(p)p/Q(p), when Q(p)≠0. It is dimensionless. A signed demand elasticity is typically negative; an absolute elasticity reports its magnitude.'),
 ('concavity','Diminishing marginal returns','Read the second derivative economically.','If f″(q)<0 throughout an interval, the function is strictly concave there and f′ is decreasing. The function itself need not be decreasing: a positive but falling derivative means increasing output with diminishing marginal gains.'),
]
SOURCES = {key: {'id':key,'title':title,'section':f'RecallLab original notes · §{i+1:02}','text':text,'version':VERSION} for i,(key,title,_,text) in enumerate(CONCEPTS)}
QUESTIONS = []
def add(concept, prompt, answer, solution, hints, *, kind='math', misconception=None, rubric=None, graph=None):
    QUESTIONS.append({'id':f'q{len(QUESTIONS)+1:02}','concept_id':concept,'prompt':prompt,'answer':answer,'solution':solution,'hints':hints,'kind':kind,'misconception':misconception or concept,'rubric':rubric or [],'source_ids':[concept],'graph':graph})
add('stationary','A firm has profit π(q) = (q − 2)³ for 0 ≤ q ≤ 4. A student says: “π′(2) = 0, so producing 2 units maximises profit.” Explain what is missing.',None,'π′(q)=3(q−2)² is nonnegative on the interval. The function increases through q=2, so this stationary point is not a local maximum. Compare the feasible endpoints: π(0)=−8 and π(4)=8. The global maximum is at q=4.', ['Does a zero derivative distinguish a maximum from a minimum or neither?','Compare the sign of 3(q−2)² on both sides of q=2.','Check the profit at q=0 and q=4 as well.'],kind='concept',rubric=['A zero first derivative alone does not prove a maximum.','The profit increases through q=2 or endpoints must be compared.'],graph={'type':'stationary','label':'π(q) = (q − 2)³'})
add('marginal','Total cost is C(q)=100+4q+q². Find marginal cost at q=3. Enter a number.','10','C′(q)=4+2q, so C′(3)=10.', ['Differentiate total cost first.','The derivative of q² is 2q.','Substitute q=3 into 4+2q.'])
add('marginal','For C(q)=q², find the exact cost change C(4)−C(3). Enter a number.','7','C(4)−C(3)=16−9=7. This differs from C′(3)=6.', ['The question asks for an exact difference.','Evaluate the original function twice.','Subtract 9 from 16.'])
add('average','Total cost is C(q)=60+6q. What is average cost at q=5?','18','Average cost is C(5)/5=90/5=18.', ['Average cost is total cost divided by output.','Compute C(5).','Divide 90 by 5.'])
add('average','For C(q)=60+6q, find marginal cost.','6','C′(q)=6. The fixed cost 60 differentiates to zero.', ['Marginal cost is a derivative.','The derivative of 60 is zero.','The slope of 6q is 6.'])
add('power','Differentiate C(q)=2q³+5q²−4q+12. Use q and explicit multiplication, such as 2*q.','6*q**2+10*q-4','C′(q)=6q²+10q−4.', ['Differentiate each term separately.','Multiply each coefficient by its exponent.','The constant 12 contributes zero.'])
add('power','For R(q)=12q−q², calculate R′(4).','4','R′(q)=12−2q, hence R′(4)=4.', ['First find the marginal revenue function.','R′(q)=12−2q.','Substitute q=4.'])
add('constant','A firm adds a fixed licence cost of 250 to C(q). By how much does marginal cost change?','0','The derivative of an output-independent constant is zero.', ['Does 250 depend on q?','Differentiate the added term only.','A constant has derivative zero.'])
add('constant','Differentiate C(q)=75+9q.','9','C′(q)=0+9=9.', ['Use the constant and linear rules.','Differentiate 75 and 9q separately.','Only the slope remains.'])
add('product','Demand price is p(q)=20−q. Revenue is p(q)*q. Find R′(q).','20-2*q','R(q)=20q−q², so R′(q)=20−2q.', ['Expand the product or use the product rule.','Price changes when quantity changes.','Differentiate 20q−q².'])
add('product','Differentiate f(q)=q*(q²+3).','3*q**2+3','f′(q)=(q²+3)+q(2q)=3q²+3.', ['Both factors depend on q.','Use u′v+uv′.','Combine q² and 2q².'])
add('chain','Differentiate f(q)=(3q+1)².','18*q+6','f′(q)=2(3q+1)*3=18q+6.', ['Differentiate the square, keeping its inside.','Multiply by the derivative of 3q+1.','Expand 6(3q+1).'])
add('chain','For f(q)=(2q+1)³, find f′(1).','54','f′(q)=6(2q+1)², so f′(1)=54.', ['The inside derivative is 2.','f′(q)=3(2q+1)²*2.','Evaluate 6*3².'])
add('profit','R(q)=20q−q² and C(q)=4q+10. Find π′(q).','16-2*q','π′(q)=(20−2q)−4=16−2q.', ['Profit is revenue minus cost.','Find MR and MC separately.','Subtract 4 from 20−2q.'])
add('profit','For π(q)=16q−q²−10, find the interior stationary quantity.','8','π′(q)=16−2q. Setting this to zero gives q=8.', ['A stationary point has zero first derivative.','Solve 16−2q=0.','Divide 16 by 2.'])
add('stationary','Find the stationary quantity of f(q)=(q−3)².','3','f′(q)=2(q−3), so the stationary quantity is q=3. It is a minimum.', ['Differentiate the square.','Set 2(q−3)=0.','Solve q−3=0.'])
add('stationary','Does f′(q)=0 alone prove that q is a maximum? Explain briefly.',None,'No. It only identifies a stationary candidate. Check derivative signs, curvature, and the feasible domain; a stationary point may also be a minimum or neither.', ['What happens at the bottom of a parabola?','Compare q² with −q² at zero.','Distinguish a candidate from a classification.'],kind='concept',rubric=['No; zero derivative alone is insufficient.','A minimum or neither is possible, or further checks are required.'])
add('second','For π(q)=16q−q²−10, calculate π″(q).','-2','π″(q)=−2, so the interior stationary point is a strict local maximum.', ['Differentiate the first derivative again.','π′(q)=16−2q.','The slope is constant.'])
add('second','At a stationary point f″(q)=0. Does the second-derivative test classify the point? Explain.',None,'No. The test is inconclusive. For example, q⁴ has a minimum at zero, −q⁴ has a maximum, and q³ has neither.', ['Compare q³ and q⁴ at zero.','Both can have zero second derivative there.','Zero curvature at the point is inconclusive.'],kind='concept',rubric=['The test is inconclusive when the second derivative is zero.','Further analysis is needed; it does not prove absence of an optimum.'])
add('boundary','Maximise f(q)=3q+1 over 0≤q≤5. Enter the maximising quantity.','5','The function increases on the whole interval, so its maximum is at q=5.', ['The domain has endpoints.','The slope is positive everywhere.','Which endpoint has the larger value?'])
add('boundary','Maximise f(q)=−(q−2)²+9 over 0≤q≤1. Enter the maximising quantity.','1','The unconstrained peak q=2 is infeasible. On [0,1] the function increases; q=1 is the constrained maximiser.', ['Is q=2 feasible?','Compare f(0) and f(1).','The right endpoint is closer to the peak.'])
add('elasticity','Demand is Q(p)=100−2p. Find signed price elasticity at p=10.','-1/4','Q′(10)=−2 and Q(10)=80. Elasticity is (−2)*10/80=−1/4.', ['Use Q′(p)*p/Q(p).','Evaluate quantity as well as its derivative.','Compute −20/80.'])
add('elasticity','Demand is Q(p)=120−3p. Find the absolute price elasticity at p=20.','1','Signed elasticity is (−3)*20/60=−1; its magnitude is 1.', ['First calculate Q(20).','Apply the point elasticity formula.','The question asks for the magnitude.'])
add('concavity','Find f″(q) for f(q)=10q−q².','-2','f′(q)=10−2q and f″(q)=−2.', ['Differentiate twice.','The first derivative is 10−2q.','Differentiate this linear function.'])
add('concavity','If f″(q)<0, must f(q) be decreasing? Explain the difference.',None,'No. A negative second derivative means the first derivative is decreasing. The function can still be increasing when its first derivative remains positive.', ['Separate the sign of the first derivative from its change.','An increasing function can have a falling slope.','Consider 10q−q² for small positive q.'],kind='concept',rubric=['No; a negative second derivative does not imply the function decreases.','The slope is decreasing, but may remain positive.'])
# Reviewed diagnostic labels. The model may select IDs, never author feedback.
MISCONCEPTIONS = {
    'stationary_is_maximum': {'description': 'Treats a zero first derivative as proof of a maximum.', 'feedback': 'A zero derivative identifies a stationary candidate. It does not establish a maximum; compare behaviour on both sides and the feasible domain.'},
    'zero_curvature_classifies': {'description': 'Treats a zero second derivative as a classification or proof that no optimum exists.', 'feedback': 'A zero second derivative makes this test inconclusive. It does not classify the point or rule out an optimum; use another check.'},
    'concave_means_decreasing': {'description': 'Confuses a decreasing slope with a decreasing function.', 'feedback': 'A falling slope can still be positive. Separate the sign of the first derivative from the sign of its change.'},
}
DIAGNOSTICS = {'q01': ['stationary_is_maximum'], 'q17': ['stationary_is_maximum'], 'q19': ['zero_curvature_classifies'], 'q25': ['concave_means_decreasing']}
for question in QUESTIONS:
    question['misconceptions'] = {key: MISCONCEPTIONS[key] for key in DIAGNOSTICS.get(question['id'], [])}

PRACTICE_QUESTIONS=QUESTIONS[:]
add('marginal','For C(q)=40+7q+2q², find marginal cost at q=2.','15','C′(q)=7+4q, so C′(2)=15.', ['Differentiate total cost.','The derivative is 7+4q.','Substitute q=2.'])
add('product','Revenue is R(q)=q*(18−2q). Find R′(q).','18-4*q','R(q)=18q−2q², giving R′(q)=18−4q.', ['Expand first.','Differentiate each term.','Differentiate −2q² carefully.'])
add('chain','Differentiate f(q)=(2q+3)².','8*q+12','f′(q)=2(2q+3)*2=8q+12.', ['Apply the chain rule.','Multiply by the inside derivative 2.','Expand 4(2q+3).'])
add('profit','For π(q)=30q−3q², find the interior stationary quantity.','5','π′(q)=30−6q. Solving 30−6q=0 gives q=5.', ['Differentiate profit.','Set the first derivative equal to zero.','Solve 30−6q=0.'])
add('boundary','Maximise f(q)=−(q−6)² over 0≤q≤3. Enter the maximising quantity.','3','The unconstrained peak is outside the domain. The function increases on [0,3], so the constrained maximum is q=3.', ['Check feasibility.','The peak at q=6 is not allowed.','Compare the endpoints.'])
CHECK_QUESTIONS=QUESTIONS[25:]
BY_ID={q['id']:q for q in QUESTIONS}
TRACKS=[{'id':'all','title':'The complete module','description':'Connect intuition, calculus, and economic decisions.','concepts':[c[0] for c in CONCEPTS]}, {'id':'foundations','title':'Think at the margin','description':'Build intuition for rates, levels, and fixed costs.','concepts':['marginal','average','constant','elasticity']}, {'id':'calculus','title':'Make the calculus click','description':'Practise power, product, and chain rules.','concepts':['power','product','chain','concavity']}, {'id':'optimisation','title':'Find the actual optimum','description':'Move beyond the first-order condition.','concepts':['stationary','profit','second','boundary']}]

def public_question(q):
    return {k:q[k] for k in ('id','concept_id','prompt','kind','graph')}

def module_info():
    return {'id':MODULE_ID,'title':'Marginal thinking','subtitle':'Derivatives & decisions in economics','version':VERSION,'question_count':len(PRACTICE_QUESTIONS),'concepts':[{'id':k,'title':t,'description':d} for k,t,d,_ in CONCEPTS],'tracks':TRACKS}
